import tkinter as tk
from tkinter import ttk
from database import get_total_income, get_total_expenses, get_balance

class DashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Financial Dashboard")

        # Create tabs
        self.tab_control = ttk.Notebook(self.root)
        self.tab_control.pack(expand=1, fill="both")

        # Create dashboard tab
        self.dashboard_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.dashboard_tab, text="Dashboard")

        # Create labels and display financial metrics
        self.total_income_label = tk.Label(self.dashboard_tab, text="Total Income:")
        self.total_income_label.pack()
        self.total_income_value = tk.Label(self.dashboard_tab, text=get_total_income())
        self.total_income_value.pack()

        self.total_expenses_label = tk.Label(self.dashboard_tab, text="Total Expenses:")
        self.total_expenses_label.pack()
        self.total_expenses_value = tk.Label(self.dashboard_tab, text=get_total_expenses())
        self.total_expenses_value.pack()

        self.balance_label = tk.Label(self.dashboard_tab, text="Balance:")
        self.balance_label.pack()
        self.balance_value = tk.Label(self.dashboard_tab, text=get_balance())
        self.balance_value.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = DashboardApp(root)
    root.mainloop()