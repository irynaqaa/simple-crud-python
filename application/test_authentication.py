import unittest
from application.authentication import Authentication

class TestAuthentication(unittest.TestCase):
    def test_authenticate(self):
        # Test with valid credentials
        auth = Authentication('admin', 'password123')
        self.assertTrue(auth.authenticate())
        
        # Test with invalid credentials
        auth = Authentication('invalid', 'invalid')
        self.assertFalse(auth.authenticate())

if __name__ == '__main__':
    unittest.main()