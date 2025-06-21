import pandas as pd
import numpy as np
from scipy import stats
from cryptography.fernet import Fernet

# Define a function to encrypt data
def encrypt_data(file_path, encryption_key):
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Perform data validation and cleaning tasks
        if df.isnull().values.any():
            print("Error: Missing values found in the data")
            return
        
        if not (df['column1'].dtype == 'int64' and df['column2'].dtype == 'object'):
            print("Error: Invalid data type in column1 or column2")
            return
        
        if not (df['column3'].apply(lambda x: len(x) == 10).all()):
            print("Error: Invalid format in column3")
            return
        
        # Encrypt the data
        cipher_suite = Fernet(encryption_key)
        cipher_text = cipher_suite.encrypt(df.to_csv(index=False).encode())
        
        return cipher_text
    
    except Exception as e:
        print(f"Error: {e}")
        return

# Define a function to decrypt data
def decrypt_data(cipher_text, encryption_key):
    try:
        # Decrypt the data
        cipher_suite = Fernet(encryption_key)
        plain_text = cipher_suite.decrypt(cipher_text)
        
        # Convert the plain text to a pandas dataframe
        df = pd.read_csv(pd.io.common.StringIO(plain_text.decode()))
        
        return df
    
    except Exception as e:
        print(f"Error: {e}")
        return
