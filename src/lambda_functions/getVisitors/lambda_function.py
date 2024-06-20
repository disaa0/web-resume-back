import json
import boto3
from decimal import Decimal
from botocore.exceptions import ClientError

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return int(obj) if obj % 1 == 0 else float(obj)
    raise TypeError

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('resume')
    
    try:
        response = table.get_item(Key={'id': 'visitors'})
        if 'Item' in response:
            visitors = response['Item'].get('visitor_count', 'visitor_count attribute not found')
            return {
                'statusCode': 200,
                'body': json.dumps({'visitors': visitors}, default=decimal_default)
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps('Item not found')
            }
    
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Unable to get item: {e.response['Error']['Message']}")
        }