import sqlite3
from datetime import datetime
from transaction import edit_transaction, delete_transaction, view_transactions
from dashboard import DashboardApp

# Connect to SQLite database. It will be created if it doesn't exist.
conn = sqlite3.connect('personal_expense_tracker.db')

# Create a cursor object
c = conn.cursor()

class PersonalExpenseTracker:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute '''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )'''
        self.cursor.execute '''CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )'''
        self.cursor.execute '''CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            category_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            date DATE NOT NULL,
            description TEXT,
            type TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (category_id) REFERENCES categories (id)
        )'''
        self.conn.commit()

    def add_user(self, name, email):
        self.cursor.execute '''INSERT INTO users (name, email) VALUES (?, ?)''', (name, email)
        self.conn.commit()

    def add_category(self, name):
        self.cursor.execute '''INSERT INTO categories (name) VALUES (?)''', (name,)
        self.conn.commit()

    def add_transaction(self, user_id, category_id, amount, date, description, type):
        self.cursor.execute '''INSERT INTO transactions (user_id, category_id, amount, date, description, type) VALUES (?, ?, ?, ?, ?, ?)''', (user_id, category_id, amount, date, description, type)
        self.conn.commit()

    def get_transactions(self, user_id):
        self.cursor.execute '''SELECT * FROM transactions WHERE user_id = ?''', (user_id,)
        return self.cursor.fetchall()

    def get_categories(self):
        self.cursor.execute '''SELECT * FROM categories'''
        return self.cursor.fetchall()

    def get_users(self):
        self.cursor.execute '''SELECT * FROM users'''
        return self.cursor.fetchall()

    def view_transactions(self, date=None, category=None, type=None):
        return view_transactions(date, category, type)

    def edit_transaction(self, transaction_id, amount=None, category_id=None, date=None, description=None, type=None):
        edit_transaction(transaction_id, amount, category_id, date, description, type)

    def delete_transaction(self, transaction_id):
        delete_transaction(transaction_id)

# Example usage
if __name__ == '__main__':
    tracker = PersonalExpenseTracker('expense_tracker.db')
    tracker.add_user('John Doe', 'john@example.com')
    tracker.add_category('Food')
    tracker.add_transaction(1, 1, 10.99, datetime.now().strftime('%Y-%m-%d'), 'Lunch', 'expense')
    print(tracker.get_transactions(1))
    print(tracker.get_categories())
    print(tracker.get_users())
    print(tracker.view_transactions())
    print(tracker.view_transactions(date='2024-09-16'))
    print(tracker.view_transactions(category=1))
    print(tracker.view_transactions(type='expense'))
    tracker.edit_transaction(1, amount=15.99)
    tracker.delete_transaction(1)
    root = tk.Tk()
    app = DashboardApp(root)
    root.mainloop()
