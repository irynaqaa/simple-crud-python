import unittest
from application.data_transformation import transform_data

class TestDataTransformation(unittest.TestCase):
    def test_transform_data(self):
        # Test with valid data
        df = transform_data('valid_data.csv')
        self.assertIsNotNone(df)
        
        # Test with invalid data
        df = transform_data('invalid_data.csv')
        self.assertIsNotNone(df)

if __name__ == '__main__':
    unittest.main()