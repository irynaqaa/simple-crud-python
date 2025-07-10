import matplotlib.pyplot as plt
from application.transaction_management import Transaction
from application.categorization import Category

class Reporting:
    """This class represents the reporting functionality of the application."""
    def __init__(self, transactions):
        self.transactions = transactions

    def generate_report(self):
        """Generates a report based on the transactions."""
        # Generate a report based on the transactions
        categories = {}
        for transaction in self.transactions:
            if transaction.category not in categories:
                categories[transaction.category] = 0
            categories[transaction.category] += float(transaction.amount)

        plt.bar(categories.keys(), categories.values())
        plt.xlabel('Category')
        plt.ylabel('Amount')
        plt.title('Spending by Category')
        plt.show()
