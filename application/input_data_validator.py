import logging
import pandas as pd
from application.encryption import Encryption

"""Module to validate input data."""

# Define the logging configuration
logging.basicConfig(filename='application/data_processing.log', level=logging.ERROR)

class InputDataValidator:
    """Class to validate input data."""
    def __init__(self, data):
        """Initialize the InputDataValidator class."""
        self.data = pd.DataFrame(data)
        self.encryption = Encryption()
    
    def validate_input_data(self):
        """Validate the input data."""
        try:
            # Define the expected format of the input data
            expected_format = {'column1': str, 'column2': int, 'column3': float}
            
            # Check if the input data matches the expected format
            if not all(isinstance(value, expected_format[key]) for key, value in self.data.items() if key in expected_format):
                raise ValueError('Invalid input data format')
            
            # Check for missing fields
            if not all(key in self.data for key in expected_format):
                raise ValueError('Missing fields in the input data')
            
            # If the input data is valid, return a pandas DataFrame
            return self.data
        except ValueError as e:
            # Catch specific exceptions instead of the general Exception
            logging.error('Error validating input data: %s', e)
            raise ValueError(f'Error validating input data: {e}') from e
