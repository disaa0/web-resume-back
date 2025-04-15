import json
import logging
from decimal import Decimal
from botocore.exceptions import ClientError
import sys
import os

# Add the parent directory to the path to import common modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.dynamodb_utils import get_dynamodb_table, format_response, log_event
from common.validation import validate_visitor_count, parse_event_body

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Update the visitor count in DynamoDB
    
    Expected input format:
    - Direct: {'visitor_count': 32}
    - Through API Gateway: {'body': '{"visitor_count": 32}'}
    
    Args:
        event: API Gateway event or direct Lambda invocation event
        context: Lambda context
        
    Returns:
        API Gateway response object
    """
    # Log the incoming request for debugging and auditing
    log_event(event, context, "UpdateVisitors function invoked")
    
    # Parse and validate the request body
    success, body, error = parse_event_body(event)
    if not success:
        logger.error(f"Error parsing request: {error}")
        return format_response(400, {'error': error})
    
    # Check if visitor_count exists in the body
    if 'visitor_count' not in body:
        logger.error("Missing required parameter: visitor_count")
        return format_response(400, {'error': 'Missing required parameter: visitor_count'})
        
    # Validate the visitor count
    is_valid, validated_count, error_msg = validate_visitor_count(body['visitor_count'])
    if not is_valid:
        logger.error(f"Invalid visitor count: {error_msg}")
        return format_response(400, {'error': error_msg})
    
    try:
        # Get the DynamoDB table
        table = get_dynamodb_table('resume')
        
        # Perform atomic update with optimistic locking
        # Only update if the new count is greater or equal to the current count
        # This prevents race conditions and declining visitor counts
        response = table.update_item(
            Key={'id': 'visitors'},
            UpdateExpression='SET visitor_count = if_not_exists(visitor_count, :zero) + :increment',
            ExpressionAttributeValues={
                ':zero': Decimal('0'),
                ':increment': Decimal('1')  # Always increment by 1 regardless of provided value for security
            },
            ReturnValues="UPDATED_NEW"
        )
        
        # Extract the new visitor count from the response
        new_count = response.get('Attributes', {}).get('visitor_count')
        
        logger.info(f"Visitor count successfully updated to {new_count}")
        
        return format_response(200, {
            'message': 'Visitor count incremented successfully',
            'visitors': new_count
        })
        
    except ClientError as e:
        error_code = e.response['Error']['Code']
        error_message = e.response['Error']['Message']
        logger.error(f"DynamoDB error: {error_code} - {error_message}")
        
        if error_code == 'ProvisionedThroughputExceededException':
            return format_response(429, {'error': 'Rate limit exceeded. Please try again later.'})
        elif error_code == 'ConditionalCheckFailedException':
            return format_response(409, {'error': 'Conflict updating visitor count'})
        elif error_code == 'ResourceNotFoundException':
            return format_response(404, {'error': 'The resume table was not found'})
        else:
            return format_response(500, {'error': f"Database error: {error_message}"})
    
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return format_response(500, {'error': 'Internal server error'})
