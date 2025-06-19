import json

def generate_json_report(data, file_path):
    # Generate the JSON report
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
