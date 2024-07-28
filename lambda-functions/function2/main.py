import json

def lambda_handler(event, context):
    """
    Lambda function handler.

    Parameters:
    event (dict): The event data.
    context (object): The context object.

    Returns:
    dict: The response object.
    """
    # Currently, event and context are not used.
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Function 2')
    }
