import json
import boto3
from botocore.exceptions import ClientError

#example input {visitor_count: 32}

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table_name = 'resume'
    table = dynamodb.Table(table_name)
    
    # Get item keys and attributes to update from the event
    key = {'id': 'visitors'}
    update_expression = 'SET visitor_count = :value'
    expression_attribute_values = {':value': event['visitor_count']}
    
    try:
        response = table.update_item(
            Key=key,
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values,
            ReturnValues="UPDATED_NEW"
        )
        return {
            'statusCode': 200,
            'body': json.dumps('Item updated successfully!'),
            'updated_attributes': response['Attributes']
        }
    except ClientError as e:
        return {
            'statusCode': 400,
            'body': json.dumps(f"Unable to update item: {e.response['Error']['Message']}")
        }