import configparser
from application.encryption import Encryption

"""Module to handle configuration."""

class Config:
    """Class to handle configuration."""
    def __init__(self, config_file):
        """Initialize the Config class."""
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        self.encryption = Encryption()
        
    def get_config(self, section, key):
        """Get the configuration value for the given section and key."""
        return self.config.get(section, key)
        
    def get_config_with_default(self, section, key, default):
        """Get the configuration value for the given section and key with a default value."""
        return self.config.get(section, key, fallback=default)
