import pandas as pd

def clean_data(file_path):
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Remove missing values
        df = df.dropna()
        
        # Remove invalid data types
        df = df[df['age'].apply(lambda x: isinstance(x, int))]
        
        return df
    
    except Exception as e:
        print(f"Error: {e}")
        return None