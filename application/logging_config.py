"""
Logging Configuration Module

This module sets up logging for the application.
"""

import logging

# Configure logging
def setup_logging():
    logging.basicConfig(filename='application.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info('Logging is set up.')


if __name__ == '__main__':
    setup_logging()
