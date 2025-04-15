import json
import logging
from decimal import Decimal

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def validate_visitor_count(visitor_count):
    """
    Validate the visitor count value
    
    Args:
        visitor_count: The value to validate
        
    Returns:
        tuple: (is_valid, validated_value, error_message)
    """
    # Check if the value exists
    if visitor_count is None:
        return False, None, "Visitor count is required"
    
    # Type validation - convert to int if possible
    try:
        # Convert to Decimal for DynamoDB compatibility
        if isinstance(visitor_count, str):
            visitor_count = visitor_count.strip()
            
        validated_count = Decimal(str(visitor_count))
        
        # Ensure it's a non-negative integer
        if validated_count < 0:
            return False, None, "Visitor count must be non-negative"
        
        if validated_count % 1 != 0:
            return False, None, "Visitor count must be an integer"
            
        # Set a reasonable upper limit to prevent abuse
        if validated_count > 1000000000:  # 1 billion
            return False, None, "Visitor count exceeds maximum allowed value"
            
        return True, validated_count, None
        
    except (ValueError, TypeError, ArithmeticError) as e:
        logger.error(f"Validation error: {str(e)}")
        return False, None, f"Invalid visitor count: {str(e)}"

def parse_event_body(event):
    """
    Parse and validate request body from API Gateway event
    
    Args:
        event: API Gateway event object
        
    Returns:
        tuple: (success, parsed_body, error_message)
    """
    try:
        # Handle both string and dict body formats
        if 'body' in event and event['body']:
            if isinstance(event['body'], str):
                body = json.loads(event['body'])
            else:
                body = event['body']
        else:
            body = event
            
        return True, body, None
    except json.JSONDecodeError as e:
        logger.error(f"JSON parsing error: {str(e)}")
        return False, None, f"Invalid JSON in request body: {str(e)}"
    except Exception as e:
        logger.error(f"Event parsing error: {str(e)}")
        return False, None, f"Error parsing request: {str(e)}"
