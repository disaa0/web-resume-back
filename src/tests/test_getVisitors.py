import unittest
from unittest.mock import patch, MagicMock
from moto import mock_aws
import boto3
import os
from botocore.exceptions import ClientError
import json
from decimal import Decimal
from lambda_functions.getVisitors.lambda_function import lambda_handler

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
        self.assertIn('headers', response)

    def test_item_not_found_creates_default(self):
        # Remove the item to simulate not found scenario
        self.table.delete_item(Key={'id': 'visitors'})
        
        event = {}
        context = {}
        response = lambda_handler(event, context)
        
        # Should return 200 with default value of 0
        self.assertEqual(response['statusCode'], 200)
        body = json.loads(response['body'])
        self.assertEqual(body['visitors'], 0)

    def test_invalid_visitor_count(self):
        # Add an item with invalid visitor count
        self.table.put_item(Item={'id': 'visitors', 'visitor_count': Decimal('-10')})
        
        event = {}
        context = {}
        response = lambda_handler(event, context)
        
        # Should return 200 but reset count to 0
        self.assertEqual(response['statusCode'], 200)
        body = json.loads(response['body'])
        self.assertEqual(body['visitors'], 0)

    @patch('lambda_functions.getVisitors.lambda_function.get_dynamodb_table')
    def test_client_error_rate_limit(self, mock_get_table):
        # Setup mock to raise rate limit error
        mock_table = MagicMock()
        mock_table.get_item.side_effect = ClientError(
            {'Error': {'Code': 'ProvisionedThroughputExceededException', 'Message': 'Rate limit exceeded'}},
            'GetItem'
        )
        mock_get_table.return_value = mock_table

        event = {}
        context = {}
        response = lambda_handler(event, context)
        
        # Should return 429 for rate limit
        self.assertEqual(response['statusCode'], 429)
        body = json.loads(response['body'])
        self.assertIn('error', body)
        self.assertIn('Rate limit exceeded', body['error'])

    @patch('lambda_functions.getVisitors.lambda_function.get_dynamodb_table')
    def test_unexpected_exception(self, mock_get_table):
        # Setup mock to raise unexpected exception
        mock_get_table.side_effect = Exception("Unexpected error")

        event = {}
        context = {}
        response = lambda_handler(event, context)
        
        # Should return 500 for unexpected errors
        self.assertEqual(response['statusCode'], 500)
        body = json.loads(response['body'])
        self.assertIn('error', body)

if __name__ == '__main__':
    unittest.main()
