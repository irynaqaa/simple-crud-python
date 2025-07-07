import pandas as pd
import numpy as np

# Define a function to process the data

def process_data(file_path):
    try:
        # Load the data from the CSV file
        data = pd.read_csv(file_path)
        # Process the data
        data['age'] = data['age'] * 2
        return data
    except Exception as e:
        print(f"Error processing data: {e}")
        return None
