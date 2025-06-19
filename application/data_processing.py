import pandas as pd
from input_validation import validate_input_data
from configuration import *

# Load the configuration from the file
config = configparser.ConfigParser()
config.read('config.ini')

# Access the configuration values
debug = config['DEFAULT']['debug']
host = config['DATABASE']['host']
database = config['DATABASE']['database']
user = config['DATABASE']['user']
password = config['DATABASE']['password']
environment = config['ENVIRONMENT']['environment']


def generate_csv_report(data, filename):
    try:
        validated_data = validate_input_data(data)
        # Create a Pandas DataFrame from the validated data
        df = pd.DataFrame([validated_data.__dict__])
        
        # Generate the CSV report
        df.to_csv(filename, index=False)
        
        print(f"CSV report generated successfully: {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
def process_data(data):
    try:
        validated_data = validate_input_data(data)
        # Perform calculations on the validated input data
        result = validated_data.id + len(validated_data.name)
        return result
    except Exception as e:
        logging.error(f"Error processing data: {e}")
        raise

if __name__ == "__main__":
    data = {
        'id': 1,
        'name': 'John Doe',
        'description': 'This is a test'
    }
    filename = 'report.csv'
    generate_csv_report(data, filename)