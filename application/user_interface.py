import tkinter as tk
from application.transaction_management import Transaction
from application.categorization import Category
from application.reporting import Reporting
from application.data_export import DataExport

class UserInterface:
    """This class represents the user interface of the application."""
    def __init__(self, root):
        self.root = root
        self.root.title('Personal Expense Tracker')
        self.transactions = []
        self.categories = []

        # Create frames
        self.frame1 = tk.Frame(self.root)
        self.frame1.pack()
        self.frame2 = tk.Frame(self.root)
        self.frame2.pack()
        self.frame3 = tk.Frame(self.root)
        self.frame3.pack()

        # Create labels and entries
        self.label1 = tk.Label(self.frame1, text='Date')
        self.label1.pack(side=tk.LEFT)
        self.entry1 = tk.Entry(self.frame1)
        self.entry1.pack(side=tk.LEFT)
        self.label2 = tk.Label(self.frame1, text='Amount')
        self.label2.pack(side=tk.LEFT)
        self.entry2 = tk.Entry(self.frame1)
        self.entry2.pack(side=tk.LEFT)
        self.label3 = tk.Label(self.frame1, text='Category')
        self.label3.pack(side=tk.LEFT)
        self.entry3 = tk.Entry(self.frame1)
        self.entry3.pack(side=tk.LEFT)
        self.label4 = tk.Label(self.frame1, text='Description')
        self.label4.pack(side=tk.LEFT)
        self.entry4 = tk.Entry(self.frame1)
        self.entry4.pack(side=tk.LEFT)

        # Create buttons
        self.button1 = tk.Button(self.frame2, text='Add Transaction', command=self.add_transaction)
        self.button1.pack(side=tk.LEFT)
        self.button2 = tk.Button(self.frame2, text='Generate Report', command=self.generate_report)
        self.button2.pack(side=tk.LEFT)
        self.button3 = tk.Button(self.frame2, text='Export to CSV', command=self.export_to_csv)
        self.button3.pack(side=tk.LEFT)

        # Create text box
        self.text_box = tk.Text(self.frame3)
        self.text_box.pack()

    def add_transaction(self):
        """Adds a new transaction to the list of transactions."""
        date = self.entry1.get()
        amount = self.entry2.get()
        category = self.entry3.get()
        description = self.entry4.get()
        transaction = Transaction(date, amount, category, description)
        self.transactions.append(transaction)
        self.text_box.insert(tk.END, str(transaction) + '
')

    def generate_report(self):
        """Generates a report based on the transactions."""
        reporting = Reporting(self.transactions)
        reporting.generate_report()

    def export_to_csv(self):
        """Exports the transactions to a CSV file."""
        data_export = DataExport(self.transactions)
        data_export.export_to_csv('transactions.csv')
