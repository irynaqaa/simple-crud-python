import logging
import os


def log_error(message):
    # Configure logging settings
    log_file = os.path.join(os.path.dirname(__file__), 'error.log')
    logging.basicConfig(
        filename=log_file,
        level=logging.ERROR,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    # Log the error message
    logging.error(message)
