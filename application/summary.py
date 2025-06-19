import sqlite3
from datetime import datetime

# Connect to SQLite database. It will be created if it doesn't exist.
conn = sqlite3.connect('personal_expense_tracker.db')

# Create a cursor object
c = conn.cursor()

def get_total_income(year, month):
    # Retrieve total income for the month
    c.execute('''
        SELECT SUM(amount)
        FROM transactions
        WHERE STRFTIME('%Y', date) = ? AND STRFTIME('%m', date) = ? AND type = 'income'
    ''', (str(year), str(month).zfill(2)))
    total_income = c.fetchone()[0]
    return total_income

def get_total_expenses(year, month):
    # Retrieve total expenses for the month
    c.execute('''
        SELECT SUM(amount)
        FROM transactions
        WHERE STRFTIME('%Y', date) = ? AND STRFTIME('%m', date) = ? AND type = 'expense'
    ''', (str(year), str(month).zfill(2)))
    total_expenses = c.fetchone()[0]
    return total_expenses

def get_balance(year, month):
    # Calculate balance by subtracting total expenses from total income
    total_income = get_total_income(year, month)
    total_expenses = get_total_expenses(year, month)
    balance = total_income - total_expenses
    return balance

def generate_monthly_summary(year, month):
    # Query to select all transactions for the given month and year
    query = "SELECT * FROM transactions WHERE STRFTIME('%Y', date) = ? AND STRFTIME('%m', date) = ?"
    c.execute(query, (year, month))
    transactions = c.fetchall()
    
    # Initialize variables to store total income, total expenses, and balance
    total_income = 0
    total_expenses = 0
    balance = 0
    
    # Iterate through each transaction
    for transaction in transactions:
        # If the transaction is an income, add it to the total income
        if transaction[5] == 'income':
            total_income += transaction[2]
        # If the transaction is an expense, add it to the total expenses
        elif transaction[5] == 'expense':
            total_expenses += transaction[2]
    
    # Calculate the balance
    balance = total_income - total_expenses
    
    # Return the monthly summary
    return total_income, total_expenses, balance

def display_summary(total_income, total_expenses, balance):
    print("Monthly Summary:")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Balance: ${balance:.2f}")

# Example usage
if __name__ == '__main__':
    year = 2024
    month = 9
    total_income, total_expenses, balance = generate_monthly_summary(year, month)
    display_summary(total_income, total_expenses, balance)
