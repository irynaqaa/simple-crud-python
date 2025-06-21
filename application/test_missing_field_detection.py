import unittest
from application.missing_field_detection import detect_missing_fields

class TestMissingFieldDetection(unittest.TestCase):
    def test_detect_missing_fields(self):
        # Test with valid data
        self.assertTrue(detect_missing_fields('valid_data.csv'))
        
        # Test with invalid data
        self.assertFalse(detect_missing_fields('invalid_data.csv'))

if __name__ == '__main__':
    unittest.main()