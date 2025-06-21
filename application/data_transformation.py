import pandas as pd

def transform_data(file_path):
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Transform the data
        df['age'] = df['age'].apply(lambda x: x * 2)
        
        return df
    
    except Exception as e:
        print(f"Error: {e}")
        return None