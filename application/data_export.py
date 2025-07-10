import csv
from application.transaction_management import Transaction


class DataExport:
    """This class represents the data export functionality of the application."""
    def __init__(self, transactions):
        self.transactions = transactions
        
    def export_to_csv(self, filename):
        """Exports the transactions to a CSV file."""
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['date', 'amount', 'category', 'description']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for transaction in self.transactions:
                writer.writerow({'date': transaction.date, 'amount': transaction.amount, 'category': transaction.category, 'description': transaction.description})
