import os
import configparser

class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(os.environ.get('CONFIG_FILE', 'config.ini'))
        
    def get_config(self, section, key):
        return self.config.get(section, key)

# Configuration file for the data processing pipeline

# Input file settings
input_file_path = 'input.csv'
input_file_type = 'csv'

# Output file settings
output_file_path = 'output.csv'
output_file_type = 'csv'

# Report settings
report_file_path = 'report.csv'
report_file_type = 'csv'

# Data validation settings
validate_data = True

# Data encryption settings
encrypt_data = True

# Add data encryption key
encryption_key = 'my_secret_key'
