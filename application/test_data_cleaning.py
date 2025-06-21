import unittest
from application.data_cleaning import clean_data

class TestDataCleaning(unittest.TestCase):
    def test_clean_data(self):
        # Test with valid data
        df = clean_data('valid_data.csv')
        self.assertIsNotNone(df)
        
        # Test with invalid data
        df = clean_data('invalid_data.csv')
        self.assertIsNotNone(df)

if __name__ == '__main__':
    unittest.main()