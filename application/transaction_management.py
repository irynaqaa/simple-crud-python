class Transaction:
    """This class represents a transaction."""
    def __init__(self, date, amount, category, description):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description
    
    def __str__(self):
        return f'Transaction(date={self.date}, amount={self.amount}, category={self.category}, description={self.description})'
