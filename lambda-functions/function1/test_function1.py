import unittest
from lambda_function1 import lambda_handler

class TestLambdaFunction1(unittest.TestCase):
    def test_lambda_handler(self):
        result = lambda_handler({}, {})
        self.assertEqual(result['statusCode'], 200)
        self.assertIn('Hello from Lambda Function 1!', result['body'])

if __name__ == '__main__':
    unittest.main()
