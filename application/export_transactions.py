import csv
import sqlite3
from datetime import datetime

def export_transactions(file_path, filter_date=None, filter_category=None, filter_type=None):
    # Connect to the SQLite database
    conn = sqlite3.connect('personal_expense_tracker.db')
    c = conn.cursor()

    # Build the query
    query = '''
        SELECT t.id, t.amount, c.name AS category, t.date, t.description, t.type, u.username AS user
        FROM transactions t
        JOIN categories c ON t.category_id = c.id
        JOIN users u ON t.user_id = u.id
    '''

    # Apply filters
    conditions = []
    params = ()
    if filter_date:
        conditions.append('t.date = ?')
        params += (filter_date,)
    if filter_category:
        conditions.append('t.category_id = ?')
        params += (filter_category,)
    if filter_type:
        conditions.append('t.type = ?')
        params += (filter_type,)

    if conditions:
        query += ' WHERE ' + ' AND '.join(conditions)

    # Execute the query
    try:
        c.execute(query, params)
        transactions = c.fetchall()
    except sqlite3.Error as e:
        print(f"Error retrieving transactions: {e}")
        return

    # Write transactions to CSV file
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['id', 'amount', 'category', 'date', 'description', 'type', 'user']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for transaction in transactions:
            writer.writerow({
                'id': transaction[0],
                'amount': transaction[1],
                'category': transaction[2],
                'date': transaction[3],
                'description': transaction[4],
                'type': transaction[5],
                'user': transaction[6]
            })

# Example usage:
export_transactions('transactions.csv', filter_date='2024-09-16')