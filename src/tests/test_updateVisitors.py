import unittest
from unittest.mock import patch, MagicMock
from moto import mock_aws
import boto3
import os
from botocore.exceptions import ClientError
import json
from lambda_functions.updateVisitors.lambda_function import lambda_handler

os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
os.environ['AWS_SECURITY_TOKEN'] = 'testing'
os.environ['AWS_SESSION_TOKEN'] = 'testing'
os.environ['AWS_DEFAULT_REGION'] = 'us-east-2'

@mock_aws
class TestLambdaHandler(unittest.TestCase):
    @patch('lambda_functions.updateVisitors.lambda_function.boto3.resource')
    def test_successful_update(self, mock_boto_resource):
        mock_dynamodb = MagicMock()
        mock_table = mock_dynamodb.Table.return_value
        mock_table.update_item.return_value = {
            'Attributes': {'id': 'visitors', 'visitor_count': 50} 
        }
        mock_boto_resource.return_value = mock_dynamodb

        event = {'visitor_count': 50} 
        context = {}

        response = lambda_handler(event, context)

        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(response['body'], json.dumps('Item updated successfully!'))
        self.assertIn('updated_attributes', response)
        self.assertEqual(response['updated_attributes'], {'id': 'visitors', 'visitor_count': 50})

    @patch('lambda_functions.updateVisitors.lambda_function.boto3.resource')
    def test_client_error(self, mock_boto_resource):
        mock_dynamodb = MagicMock()
        mock_table = mock_dynamodb.Table.return_value
        mock_table.update_item.side_effect = ClientError(
            {'Error': {'Message': 'The conditional request failed'}},
            'UpdateItem'
        )
        mock_boto_resource.return_value = mock_dynamodb

        event = {'visitor_count': 50}
        context = {}

        response = lambda_handler(event, context)

        self.assertEqual(response['statusCode'], 400)
        self.assertEqual(response['body'], json.dumps("Unable to update item: The conditional request failed"))


if __name__ == '__main__':
    unittest.main()
