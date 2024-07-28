# lambda2/test_handler.py
from handler import lambda_handler

def test_lambda_handler():
    response = lambda_handler({}, {})
    assert response['statusCode'] == 200
    assert response['body'] == 'Hello from Lambda 2!'
