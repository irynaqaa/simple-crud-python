import json
import pandas as pd
from application.encryption import Encryption

"""Module to generate JSON reports using json library."""

class JsonReportGenerator:
    """Class to generate JSON reports."""
    def __init__(self, data):
        """Initialize the JsonReportGenerator class."""
        self.data = pd.DataFrame(data)
        self.encryption = Encryption()
    
    def generate_json_report(self):
        """Generate a JSON report from the given data."""
        # Implement JSON report generation logic here
        return self.data.to_json(orient='records')
    
    def generate_json_report_with_pretty_print(self):
        """Generate a JSON report with pretty print from the given data."""
        # Implement JSON report generation logic here
        return self.data.to_json(orient='records', indent=4)
