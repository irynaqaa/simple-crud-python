import argparse
import pandas as pd
import numpy as np
from scipy import stats
from application.data_encryption import encrypt_data, decrypt_data
from application.config import Config

# Define a function to validate data format
def validate_data_format(file_path):
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Check for missing values
        if df.isnull().values.any():
            print("Error: Missing values found in the data")
            return False
        
        # Check for invalid data types
        if not (df['column1'].dtype == 'int64' and df['column2'].dtype == 'object'):
            print("Error: Invalid data type in column1 or column2")
            return False
        
        # Check for incorrect formats
        if not (df['column3'].apply(lambda x: len(x) == 10).all()):
            print("Error: Invalid format in column3")
            return False
        
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        return False

# Define a function to generate CSV report
def generate_csv_report(file_path):
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Perform data validation and cleaning tasks
        if df.isnull().values.any():
            print("Error: Missing values found in the data")
            return False
        
        if not (df['column1'].dtype == 'int64' and df['column2'].dtype == 'object'):
            print("Error: Invalid data type in column1 or column2")
            return False
        
        if not (df['column3'].apply(lambda x: len(x) == 10).all()):
            print("Error: Invalid format in column3")
            return False
        
        # Generate the CSV report
        report_file_path = 'report.csv'
        df.to_csv(report_file_path, index=False)
        
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        return False

# Define a function to generate JSON report
def generate_json_report(file_path):
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Perform data validation and cleaning tasks
        if df.isnull().values.any():
            print("Error: Missing values found in the data")
            return False
        
        if not (df['column1'].dtype == 'int64' and df['column2'].dtype == 'object'):
            print("Error: Invalid data type in column1 or column2")
            return False
        
        if not (df['column3'].apply(lambda x: len(x) == 10).all()):
            print("Error: Invalid format in column3")
            return False
        
        # Generate the JSON report
        report_file_path = 'report.json'
        df.to_json(report_file_path, orient='records')
        
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        return False

# Define a main function to handle command-line arguments
def main():
    parser = argparse.ArgumentParser(description='Data Processing Pipeline')
    parser.add_argument('--input_file', help='Input CSV file')
    parser.add_argument('--output_file', help='Output report file')
    parser.add_argument('--report_type', help='Type of report (CSV or JSON)')
    args = parser.parse_args()
    
    if args.report_type == 'CSV':
        generate_csv_report(args.input_file)
    elif args.report_type == 'JSON':
        generate_json_report(args.input_file)
    else:
        print("Error: Invalid report type")

    # Load configuration
    config = Config()
    
    # Get encryption key from configuration
    encryption_key = config.get_config('encryption', 'key')
    
    # Encrypt the data
    encrypted_data = encrypt_data(args.input_file, encryption_key)
    
    # Decrypt the data
    decrypted_data = decrypt_data(encrypted_data, encryption_key)
    
    print("Data encrypted and decrypted successfully")

if __name__ == '__main__':
    main()
