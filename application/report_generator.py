import pandas as pd
import numpy as np
from scipy import stats

def generate_report(file_path):
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Perform data validation and cleaning tasks
        if df.isnull().values.any():
            print("Error: Missing values found in the data")
            return False
        
        if not (df['column1'].dtype == 'int64' and df['column2'].dtype == 'object'):
            print("Error: Invalid data type in column1 or column2")
            return False
        
        if not (df['column3'].apply(lambda x: len(x) == 10).all()):
            print("Error: Invalid format in column3")
            return False
        
        # Generate the report
        report_file_path = 'report.csv'
        df.to_csv(report_file_path, index=False)
        
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        return False