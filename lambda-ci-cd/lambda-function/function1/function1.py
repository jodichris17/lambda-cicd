import json

def lambda_handler(event, context):
    # Your Lambda function code
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda Function 1!')
    }
