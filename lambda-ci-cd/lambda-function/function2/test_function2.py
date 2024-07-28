import unittest
from lambda_function2 import lambda_handler

class TestLambdaFunction2(unittest.TestCase):
    def test_lambda_handler(self):
        result = lambda_handler({}, {})
        self.assertEqual(result['statusCode'], 200)
        self.assertIn('Hello from Lambda Function 2!', result['body'])

if __name__ == '__main__':
    unittest.main()
