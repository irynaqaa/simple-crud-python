from configuration import Configuration
from validation import load_data, validate_data, handle_validation_errors, format_specs
from data_processing import process_data
from validation import validate_data_for_report
from json_report import generate_json_report
import argparse
import json
import csv


class Main:
    def __init__(self):
        self.config = Configuration()
        self.run()
    
    def run(self):
        # Define the command-line arguments and options
        parser = argparse.ArgumentParser(description='My Command-Line Interface')
        parser.add_argument('-c', '--command', help='Specify the command to run')
        parser.add_argument('-o', '--output', help='Specify the output file')
        args = parser.parse_args()
        
        # Implement the logic for each command-line argument and option
        if args.command == 'generate_json_report':
            # Generate a JSON report
            data = {
                'name': 'John',
                'age': 25,
                'city': 'New York'
            }
            generate_json_report(data, args.output)
            print(f"JSON report generated successfully: {args.output}")
        elif args.command == 'generate_csv_report':
            # Generate a CSV report
            data = {
                'name': ['John', 'Mary', 'David'],
                'age': [25, 31, 42],
                'city': ['New York', 'Los Angeles', 'Chicago']
            }
            with open(args.output, 'w') as file:
                writer = csv.writer(file)
                writer.writerow(['name', 'age', 'city'])
                for row in zip(data['name'], data['age'], data['city']):
                    writer.writerow(row)
            print(f"CSV report generated successfully: {args.output}")
        else:
            print("Invalid command. Please specify a valid command.")
        
        file_path = 'data.csv'
        data = load_data(file_path)
        try:
            validate_data(data, format_specs)
            # Process the data
            data = process_data(file_path)
            # Validate the data
            if validate_data_for_report(data):
                # Generate the report
                data.to_csv('report.csv', index=False)
                print("Report generated successfully")
            else:
                print("Error: Data is not valid")
        except ValueError as e:
            handle_validation_errors([str(e)])


if __name__ == '__main__':
    Main()
