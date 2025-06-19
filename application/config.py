import os


def get_config():
    """Retrieve configuration settings from environment variables."""
    config = {
        'DB_HOST': os.getenv('DB_HOST', 'localhost'),
        'DB_PORT': os.getenv('DB_PORT', '5432'),
        'DB_USER': os.getenv('DB_USER', 'user'),
        'DB_PASSWORD': os.getenv('DB_PASSWORD', 'password'),
    }
    return config
