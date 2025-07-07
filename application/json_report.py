import json

def generate_json_report(data: dict, filename: str) -> None:
    """
    Generate a JSON report from the given data.

    Parameters:
    data (dict): Input data dictionary.
    filename (str): Output JSON filename.
    """
    try:
        # Convert the data to JSON format
        json_content = json.dumps(data, indent=4)
        # Write the JSON content to a file
        with open(filename, 'w') as file:
            file.write(json_content)
        print(f"JSON report generated successfully: {filename}")
    except Exception as e:
        print(f"Error generating JSON report: {e}")
