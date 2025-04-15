import boto3
import json
from decimal import Decimal
from botocore.exceptions import ClientError
import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

class DecimalEncoder(json.JSONEncoder):
    """Custom JSON encoder for Decimal types"""
    def default(self, obj):
        if isinstance(obj, Decimal):
            return int(obj) if obj % 1 == 0 else float(obj)
        return super(DecimalEncoder, self).default(obj)

def get_dynamodb_table(table_name='resume'):
    """Get DynamoDB table resource with error handling"""
    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(table_name)
        return table
    except Exception as e:
        logger.error(f"Error connecting to DynamoDB: {str(e)}")
        raise

def format_response(status_code, body, headers=None):
    """Create a standardized API response"""
    response = {
        'statusCode': status_code,
        'body': json.dumps(body, cls=DecimalEncoder)
    }
    
    # Add CORS and other headers if provided
    if headers:
        response['headers'] = headers
    else:
        response['headers'] = {
            'Access-Control-Allow-Origin': 'https://disaa.dev',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'
        }
    
    return response

def log_event(event, context, message="Lambda function invoked"):
    """Log event details for debugging and auditing"""
    logger.info(f"{message}: {json.dumps(event)}")
    if context:
        logger.info(f"RequestId: {context.aws_request_id}")
