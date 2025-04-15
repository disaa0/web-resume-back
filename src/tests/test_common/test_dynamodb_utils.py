import unittest
from unittest.mock import patch, MagicMock
import sys
import os
import json
from decimal import Decimal

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from lambda_functions.common.dynamodb_utils import get_dynamodb_table, format_response, DecimalEncoder

class TestDynamoDBUtils(unittest.TestCase):
    @patch('lambda_functions.common.dynamodb_utils.boto3.resource')
    def test_get_dynamodb_table(self, mock_resource):
        # Setup mock
        mock_table = MagicMock()
        mock_dynamodb = MagicMock()
        mock_dynamodb.Table.return_value = mock_table
        mock_resource.return_value = mock_dynamodb
        
        # Call function
        result = get_dynamodb_table('test_table')
        
        # Verify results
        mock_resource.assert_called_once_with('dynamodb')
        mock_dynamodb.Table.assert_called_once_with('test_table')
        self.assertEqual(result, mock_table)
    
    @patch('lambda_functions.common.dynamodb_utils.boto3.resource')
    def test_get_dynamodb_table_exception(self, mock_resource):
        # Setup mock to raise exception
        mock_resource.side_effect = Exception("Connection error")
        
        # Verify exception is raised
        with self.assertRaises(Exception):
            get_dynamodb_table('test_table')
    
    def test_format_response(self):
        # Test with simple data
        response = format_response(200, {'message': 'success'})
        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(json.loads(response['body']), {'message': 'success'})
        self.assertIn('headers', response)
        
        # Test with custom headers
        custom_headers = {'X-Custom-Header': 'value'}
        response = format_response(201, {'id': 123}, custom_headers)
        self.assertEqual(response['statusCode'], 201)
        self.assertEqual(json.loads(response['body']), {'id': 123})
        self.assertEqual(response['headers'], custom_headers)
        
        # Test with Decimal values
        data_with_decimal = {'count': Decimal('42.0'), 'integers': [Decimal('1'), Decimal('2')]}
        response = format_response(200, data_with_decimal)
        body = json.loads(response['body'])
        self.assertEqual(body['count'], 42)
        self.assertEqual(body['integers'], [1, 2])
    
    def test_decimal_encoder(self):
        # Test integer decimal
        self.assertEqual(json.dumps(Decimal('42'), cls=DecimalEncoder), '42')
        
        # Test float decimal
        self.assertEqual(json.dumps(Decimal('3.14'), cls=DecimalEncoder), '3.14')
        
        # Test regular value
        self.assertEqual(json.dumps("test", cls=DecimalEncoder), '"test"')
        
        # Test list with decimals
        self.assertEqual(
            json.dumps([Decimal('1'), Decimal('2.5')], cls=DecimalEncoder), 
            '[1, 2.5]'
        )
        
        # Test dict with decimals
        self.assertEqual(
            json.dumps({"a": Decimal('1'), "b": Decimal('2.5')}, cls=DecimalEncoder),
            '{"a": 1, "b": 2.5}'
        )

if __name__ == '__main__':
    unittest.main()
