# lambda1/handler.py
def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda 1!'
    }