from pydantic import BaseModel, ValidationError
from typing import Optional
from pathlib import Path
import os
import re
import logging
from configuration import *

logging.basicConfig(level=logging.INFO)

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


class InputData(BaseModel):
    id: int
    name: str
    description: Optional[str]
    

def validate_input_data_format(input_data, expected_format):
    try:
        if re.match(expected_format, input_data):
            return True
        else:
            raise ValueError("Invalid input data format")
    except Exception as e:
        logging.error(f"Error validating input data format: {e}")
        raise


def check_missing_fields(input_data, required_fields):
    try:
        for field in required_fields:
            if field not in input_data:
                raise ValueError(f"Missing required field: {field}")
        return True
    except Exception as e:
        logging.error(f"Error checking missing fields: {e}")
        raise


def validate_input_data(data):
    try:
        input_data = InputData(**data)
        return input_data
    except ValidationError as e:
        raise ValueError("Invalid input data format") from e