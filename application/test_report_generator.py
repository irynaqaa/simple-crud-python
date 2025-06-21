import unittest
from application.report_generator import generate_report

class TestReportGenerator(unittest.TestCase):
    def test_generate_report(self):
        # Test with valid data
        self.assertTrue(generate_report('valid_data.csv'))
        
        # Test with invalid data
        self.assertFalse(generate_report('invalid_data.csv'))

if __name__ == '__main__':
    unittest.main()