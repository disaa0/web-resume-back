import unittest
import sys
import os
import json
from decimal import Decimal

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from lambda_functions.common.validation import validate_visitor_count, parse_event_body

class TestValidation(unittest.TestCase):
    def test_valid_visitor_count(self):
        test_cases = [
            (0, True),
            (1, True),
            (100, True),
            ("42", True),
            (" 50 ", True),  # With whitespace
            (999999, True)
        ]
        
        for value, expected_valid in test_cases:
            is_valid, validated_count, error_msg = validate_visitor_count(value)
            self.assertEqual(is_valid, expected_valid, f"Failed for value: {value}")
            if is_valid:
                self.assertIsInstance(validated_count, Decimal)
                self.assertEqual(float(validated_count), float(value))
    
    def test_invalid_visitor_count(self):
        test_cases = [
            (None, False),
            (-1, False),
            (1.5, False),  # Non-integer
            ("abc", False),
            (float('inf'), False),
            (2000000000, False)  # Over limit
        ]
        
        for value, expected_valid in test_cases:
            is_valid, validated_count, error_msg = validate_visitor_count(value)
            self.assertEqual(is_valid, expected_valid, f"Failed for value: {value}")
            self.assertIsNotNone(error_msg)
            
    def test_parse_event_body_string_json(self):
        # Test with string JSON body (API Gateway format)
        event = {
            'body': json.dumps({'visitor_count': 42})
        }
        
        success, body, error = parse_event_body(event)
        self.assertTrue(success)
        self.assertEqual(body['visitor_count'], 42)
        self.assertIsNone(error)
    
    def test_parse_event_body_direct(self):
        # Test with direct invocation format
        event = {'visitor_count': 42}
        
        success, body, error = parse_event_body(event)
        self.assertTrue(success)
        self.assertEqual(body['visitor_count'], 42)
        self.assertIsNone(error)
    
    def test_parse_event_body_invalid_json(self):
        # Test with invalid JSON
        event = {
            'body': '{"visitor_count": 42'  # Missing closing brace
        }
        
        success, body, error = parse_event_body(event)
        self.assertFalse(success)
        self.assertIsNone(body)
        self.assertIsNotNone(error)

if __name__ == '__main__':
    unittest.main()
