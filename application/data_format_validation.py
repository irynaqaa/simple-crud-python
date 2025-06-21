import pandas as pd
import numpy as np
from scipy import stats

def validate_data_format(file_path):
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Check for missing values
        if df.isnull().values.any():
            print("Error: Missing values found in the data")
            return False
        
        # Check for invalid data types
        if not (df['column1'].dtype == 'int64' and df['column2'].dtype == 'object'):
            print("Error: Invalid data type in column1 or column2")
            return False
        
        # Check for incorrect formats
        if not (df['column3'].apply(lambda x: len(x) == 10).all()):
            print("Error: Invalid format in column3")
            return False
        
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        return False