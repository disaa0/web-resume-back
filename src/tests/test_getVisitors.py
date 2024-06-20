import unittest
from unittest.mock import patch, MagicMock
from moto import mock_aws
import boto3
import os
from botocore.exceptions import ClientError
import json
from decimal import Decimal
from lambda_functions.getVisitors.lambda_function import lambda_handler, decimal_default

os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
os.environ['AWS_SECURITY_TOKEN'] = 'testing'
os.environ['AWS_SESSION_TOKEN'] = 'testing'
os.environ['AWS_DEFAULT_REGION'] = 'us-east-2'

@mock_aws
class TestLambdaHandler(unittest.TestCase):

    def setUp(self):
        # Create a mock DynamoDB table
        self.dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
        self.table = self.dynamodb.create_table(
            TableName='resume',
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        )
        self.table.meta.client.get_waiter('table_exists').wait(TableName='resume')
        # Insert a mock item
        self.table.put_item(Item={'id': 'visitors', 'visitor_count': Decimal('123')})

    def test_successful_retrieval(self):
        event = {}
        context = {}
        response = lambda_handler(event, context)
        self.assertEqual(response['statusCode'], 200)
        body = json.loads(response['body'])
        self.assertEqual(body['visitors'], 123)

    def test_item_not_found(self):
        # Remove the item to simulate not found scenario
        self.table.delete_item(Key={'id': 'visitors'})
        
        event = {}
        context = {}
        response = lambda_handler(event, context)
        self.assertEqual(response['statusCode'], 404)
        body = json.loads(response['body'])
        self.assertEqual(body, 'Item not found')

    @patch('lambda_functions.getVisitors.lambda_function.boto3.resource')
    def test_client_error(self, mock_boto_resource):
        mock_dynamodb = MagicMock()
        mock_table = mock_dynamodb.Table.return_value
        mock_table.get_item.side_effect = ClientError(
            {'Error': {'Message': 'An error occurred'}},
            'GetItem'
        )
        mock_boto_resource.return_value = mock_dynamodb

        event = {}
        context = {}
        response = lambda_handler(event, context)
        self.assertEqual(response['statusCode'], 500)
        body = json.loads(response['body'])
        self.assertEqual(body, 'Unable to get item: An error occurred')

if __name__ == '__main__':
    unittest.main()
