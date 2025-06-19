"""
Configuration Management Module

This module defines configuration parameters and reads settings from
config files and environment variables.
"""

import os
import logging

# Configure logging
logging.basicConfig(filename='application.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def read_config():
    """
    Reads configuration settings from environment variables.
    :return: A dictionary of configuration settings.
    """
    config = {
        'param1': os.getenv('PARAM1', 'default_value1'),
        'param2': os.getenv('PARAM2', 'default_value2'),
    }
    logging.info('Configuration settings read successfully.')
    return config


if __name__ == '__main__':
    config = read_config()
    print(config)
