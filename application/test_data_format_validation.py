import unittest
from application.data_format_validation import validate_data_format

class TestDataFormatValidation(unittest.TestCase):
    def test_validate_data_format(self):
        # Test with valid data
        self.assertTrue(validate_data_format('valid_data.csv'))
        
        # Test with invalid data
        self.assertFalse(validate_data_format('invalid_data.csv'))

if __name__ == '__main__':
    unittest.main()