"""
Reporting Module

This module generates summary reports in both CSV and JSON formats based on
the processed data.
"""

import csv
import json
import logging

# Configure logging
logging.basicConfig(filename='application.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def generate_csv_report(data, file_path):
    """
    Generates a CSV report from the processed data.

    :param data: The processed data to be reported.
    :param file_path: The path where the CSV report will be saved.
    """
    try:
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Field1', 'Field2', 'Field3'])  # Header
            for row in data:
                writer.writerow(row)
        logging.info('CSV report generated successfully: %s', file_path)
    except Exception as e:
        logging.error('Error generating CSV report: %s', e)

def generate_json_report(data, file_path):
    """
    Generates a JSON report from the processed data.

    :param data: The processed data to be reported.
    :param file_path: The path where the JSON report will be saved.
    """
    try:
        with open(file_path, 'w') as jsonfile:
            json.dump(data, jsonfile)
        logging.info('JSON report generated successfully: %s', file_path)
    except Exception as e:
        logging.error('Error generating JSON report: %s', e)


if __name__ == '__main__':
    # Example usage
    sample_data = [[1, 2, 3], [4, 5, 6]]  # Replace with actual processed data
    generate_csv_report(sample_data, 'report.csv')
    generate_json_report(sample_data, 'report.json')
