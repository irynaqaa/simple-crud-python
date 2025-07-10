import os
import hashlib
from cryptography.fernet import Fernet

"""Module to handle encryption."""

class Encryption:
    """Class to handle encryption."""
    def __init__(self, key=None):
        """Initialize the Encryption class."""
        if key is None:
            key = Fernet.generate_key()
        self.key = key
        self.cipher_suite = Fernet(self.key)
    
    def encrypt(self, data):
        """Encrypt the data."""
        cipher_text = self.cipher_suite.encrypt(data.encode())
        return cipher_text
    
    def decrypt(self, cipher_text):
        """Decrypt the cipher text."""
        plain_text = self.cipher_suite.decrypt(cipher_text)
        return plain_text.decode()
