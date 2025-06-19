import os
import hashlib

def encrypt_data(data):
    # Generate a key
    key = hashlib.sha256(os.urandom(60)).hexdigest()
    # Encrypt the data
    encrypted_data = hashlib.sha256((data + key).encode()).hexdigest()
    return encrypted_data

def decrypt_data(encrypted_data, key):
    # Decrypt the data
    decrypted_data = hashlib.sha256((encrypted_data + key).encode()).hexdigest()
    return decrypted_data
