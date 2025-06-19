"""
File Upload Module

This module handles the file upload functionality, including validation of the
uploaded files and checking for missing fields.
"""

import os
import logging

# Configure logging
logging.basicConfig(filename='application.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def upload_file(file_path):
    """
    Uploads a file and validates its format.

    :param file_path: Path to the file to be uploaded.
    :return: A tuple indicating success and error message if any.
    """
    if not os.path.isfile(file_path):
        logging.error('File not found: %s', file_path)
        return False, 'File not found.'

    # Validate file format
    if not file_path.endswith('.csv'):
        logging.error('Invalid file format: %s', file_path)
        return False, 'Invalid file format. Only CSV files are allowed.'

    # Check for missing fields (example check)
    with open(file_path, 'r') as file:
        header = file.readline().strip().split(',')
        required_fields = ['field1', 'field2', 'field3']
        missing_fields = [field for field in required_fields if field not in header]
        if missing_fields:
            logging.error('Missing fields: %s', missing_fields)
            return False, f'Missing fields: {','.join(missing_fields)}'

    logging.info('File uploaded successfully: %s', file_path)
    return True, 'File uploaded successfully.'


if __name__ == '__main__':
    # Example usage
    result, message = upload_file('data.csv')
    print(message)
