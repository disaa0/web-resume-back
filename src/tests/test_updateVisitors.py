import unittest
from unittest.mock import patch, MagicMock
from moto import mock_aws
import boto3
import os
from botocore.exceptions import ClientError
import json
from decimal import Decimal
from lambda_functions.updateVisitors.lambda_function import lambda_handler

os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
os.environ['AWS_SECURITY_TOKEN'] = 'testing'
os.environ['AWS_SESSION_TOKEN'] = 'testing'
os.environ['AWS_DEFAULT_REGION'] = 'us-east-2'

@mock_aws
class TestLambdaHandler(unittest.TestCase):
    @patch('lambda_functions.updateVisitors.lambda_function.get_dynamodb_table')
    def test_successful_update(self, mock_get_table):
        # Setup mock table
        mock_table = MagicMock()
        mock_table.update_item.return_value = {
            'Attributes': {'visitor_count': Decimal('42')}
        }
        mock_get_table.return_value = mock_table

        # Test direct invocation format
        event = {'visitor_count': 42}
        context = {}

        response = lambda_handler(event, context)

        # Verify response
        self.assertEqual(response['statusCode'], 200)
        body = json.loads(response['body'])
        self.assertEqual(body['message'], 'Visitor count incremented successfully')
        self.assertEqual(body['visitors'], 42)

        # Verify the update_item call used atomic increment
        mock_table.update_item.assert_called_once()
        call_args = mock_table.update_item.call_args[1]
        self.assertEqual(call_args['Key'], {'id': 'visitors'})
        self.assertEqual(call_args['UpdateExpression'], 'SET visitor_count = if_not_exists(visitor_count, :zero) + :increment')
        self.assertEqual(call_args['ExpressionAttributeValues'][':increment'], Decimal('1'))

    @patch('lambda_functions.updateVisitors.lambda_function.get_dynamodb_table')
    def test_api_gateway_format(self, mock_get_table):
        # Setup mock table
        mock_table = MagicMock()
        mock_table.update_item.return_value = {
            'Attributes': {'visitor_count': Decimal('42')}
        }
        mock_get_table.return_value = mock_table

        # Test API Gateway format
        event = {
            'body': json.dumps({'visitor_count': 42})
        }
        context = {}

        response = lambda_handler(event, context)

        # Verify response
        self.assertEqual(response['statusCode'], 200)
        self.assertIn('headers', response)

    def test_invalid_input(self):
        # Test with missing visitor_count
        event = {'something_else': 42}
        context = {}

        response = lambda_handler(event, context)

        self.assertEqual(response['statusCode'], 400)
        body = json.loads(response['body'])
        self.assertIn('error', body)

    def test_negative_visitor_count(self):
        # Test with negative value
        event = {'visitor_count': -10}
        context = {}

        response = lambda_handler(event, context)

        self.assertEqual(response['statusCode'], 400)
        body = json.loads(response['body'])
        self.assertIn('error', body)

    @patch('lambda_functions.updateVisitors.lambda_function.get_dynamodb_table')
    def test_client_error(self, mock_get_table):
        # Setup mock to raise ClientError
        mock_table = MagicMock()
        mock_table.update_item.side_effect = ClientError(
            {'Error': {'Code': 'ProvisionedThroughputExceededException', 'Message': 'Rate limit exceeded'}},
            'UpdateItem'
        )
        mock_get_table.return_value = mock_table

        event = {'visitor_count': 42}
        context = {}

        response = lambda_handler(event, context)

        self.assertEqual(response['statusCode'], 429)
        body = json.loads(response['body'])
        self.assertIn('error', body)
        self.assertIn('Rate limit exceeded', body['error'])

    @patch('lambda_functions.updateVisitors.lambda_function.get_dynamodb_table')
    def test_unexpected_exception(self, mock_get_table):
        # Setup mock to raise unexpected exception
        mock_get_table.side_effect = Exception("Unexpected error")

        event = {'visitor_count': 42}
        context = {}

        response = lambda_handler(event, context)

        self.assertEqual(response['statusCode'], 500)
        body = json.loads(response['body'])
        self.assertIn('error', body)

if __name__ == '__main__':
    unittest.main()
