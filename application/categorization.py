class Category:
    """This class represents a category of transactions."""
    def __init__(self, name):
        self.name = name
        self.transactions = []
        
    def add_transaction(self, transaction):
        """Adds a transaction to the category."""
        self.transactions.append(transaction)
    
    def __str__(self):
        return f'Category(name={self.name}, transactions={self.transactions})'
