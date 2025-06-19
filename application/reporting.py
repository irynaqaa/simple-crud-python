import json
import csv


def generate_csv_report(data, file_path):
    """Generate a CSV report from the processed data."""
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write header
        writer.writerow(data[0].keys())
        # Write data rows
        for item in data:
            writer.writerow(item.values())


def generate_json_report(data, file_path):
    """Generate a JSON report from the processed data."""
    with open(file_path, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)
