import sqlite3
from datetime import datetime

# Connect to SQLite database. It will be created if it doesn't exist.
conn = sqlite3.connect('personal_expense_tracker.db')

# Create a cursor object
c = conn.cursor()

def edit_transaction(transaction_id, amount=None, category_id=None, date=None, description=None, type=None):
    # Query to update a transaction
    query = "UPDATE transactions SET"
    params = {}
    if amount:
        query += " amount = :amount"
        params['amount'] = amount
    if category_id:
        if 'amount' in params:
            query += ", category_id = :category_id"
        else:
            query += " category_id = :category_id"
        params['category_id'] = category_id
    if date:
        if 'amount' in params or 'category_id' in params:
            query += ", date = :date"
        else:
            query += " date = :date"
        params['date'] = date
    if description:
        if 'amount' in params or 'category_id' in params or 'date' in params:
            query += ", description = :description"
        else:
            query += " description = :description"
        params['description'] = description
    if type:
        if 'amount' in params or 'category_id' in params or 'date' in params or 'description' in params:
            query += ", type = :type"
        else:
            query += " type = :type"
        params['type'] = type
    query += " WHERE id = :id"
    params['id'] = transaction_id
    try:
        c.execute(query, params)
        conn.commit()
        print("Transaction edited successfully.")
    except sqlite3.Error as e:
        print(f"Error editing transaction: {e}")
    finally:
        conn.close()


def delete_transaction(transaction_id):
    # Query to delete a transaction
    query = "DELETE FROM transactions WHERE id = ?"
    try:
        c.execute(query, (transaction_id,))
        conn.commit()
        print("Transaction deleted successfully.")
    except sqlite3.Error as e:
        print(f"Error deleting transaction: {e}")
    finally:
        conn.close()


def view_transactions(date=None, category=None, type=None):
    # Query to select all transactions
    query = "SELECT * FROM transactions"
    params = {}
    if date:
        query += " WHERE date = :date"
        params['date'] = date
    if category:
        if 'date' in params:
            query += " AND category_id = :category"
        else:
            query += " WHERE category_id = :category"
        params['category'] = category
    if type:
        if 'date' in params or 'category' in params:
            query += " AND type = :type"
        else:
            query += " WHERE type = :type"
        params['type'] = type
    try:
        c.execute(query, params)
        transactions = c.fetchall()
        return transactions
    except sqlite3.Error as e:
        print(f"Error viewing transactions: {e}")
    finally:
        conn.close()
