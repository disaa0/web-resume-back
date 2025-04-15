import json
import logging
from decimal import Decimal
from botocore.exceptions import ClientError
import sys
import os

# Add the parent directory to the path to import common modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.dynamodb_utils import get_dynamodb_table, format_response, log_event

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Retrieve the visitor count from DynamoDB
    
    Args:
        event: API Gateway event
        context: Lambda context
        
    Returns:
        API Gateway response object
    """
    # Log the incoming request for debugging and auditing
    log_event(event, context, "GetVisitors function invoked")
    
    try:
        # Get the DynamoDB table
        table = get_dynamodb_table('resume')
        
        # Retrieve the visitor count
        response = table.get_item(Key={'id': 'visitors'})
        
        # Check if the item exists
        if 'Item' in response:
            # Get the visitor count, defaulting to 0 if not found
            visitors = response['Item'].get('visitor_count', 0)
            
            # Validate that the visitor count is a non-negative integer
            if isinstance(visitors, Decimal) and visitors >= 0:
                return format_response(200, {'visitors': visitors})
            else:
                # If the visitor count is invalid, reset it to 0
                logger.warning(f"Invalid visitor count found: {visitors}. Returning 0.")
                return format_response(200, {'visitors': 0})
        else:
            # Create the item if it doesn't exist
            logger.info("Visitors item not found. Creating with count 0.")
            
            try:
                table.put_item(
                    Item={'id': 'visitors', 'visitor_count': Decimal('0')},
                    ConditionExpression='attribute_not_exists(id)'
                )
                return format_response(200, {'visitors': 0})
            except ClientError as put_error:
                # Handle race conditions where the item was created between our check and put
                if put_error.response['Error']['Code'] == 'ConditionalCheckFailedException':
                    # Try to get the item again
                    retry_response = table.get_item(Key={'id': 'visitors'})
                    if 'Item' in retry_response:
                        visitors = retry_response['Item'].get('visitor_count', 0)
                        return format_response(200, {'visitors': visitors})
                
                # For other errors, raise to be caught by the outer exception handler
                raise
    
    except ClientError as e:
        error_code = e.response['Error']['Code']
        error_message = e.response['Error']['Message']
        logger.error(f"DynamoDB error: {error_code} - {error_message}")
        
        if error_code == 'ProvisionedThroughputExceededException':
            return format_response(429, {'error': 'Rate limit exceeded. Please try again later.'})
        elif error_code == 'ResourceNotFoundException':
            return format_response(404, {'error': 'The resume table was not found'})
        else:
            return format_response(500, {'error': f"Database error: {error_message}"})
    
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return format_response(500, {'error': 'Internal server error'})
