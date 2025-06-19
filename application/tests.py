import unittest
from data_processing import algorithm_x, validate_data


class TestDataProcessing(unittest.TestCase):
    def test_algorithm_x(self):
        input_data = [{'required_field': 'value1'}, {'required_field': 'value2'}]
        expected_output = [{'required_field': 'value1'}, {'required_field': 'value2'}]
        self.assertEqual(algorithm_x(input_data), expected_output)

    def test_validate_data(self):
        valid_data = [{'required_field': 'value1'}, {'required_field': 'value2'}]
        invalid_data = [{'missing_field': 'value1'}]
        validate_data(valid_data)  # Should not raise
        with self.assertRaises(ValueError):
            validate_data(invalid_data)


if __name__ == '__main__':
    unittest.main()
