import pandas as pd

def validate_data(file_path):
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Check for missing values
        if df.isnull().values.any():
            print("Error: Missing values found in the data")
            return False
        
        # Check for invalid data types
        if not (df['age'].dtype == 'int64'):
            print("Error: Invalid data type in age column")
            return False
        
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        return False