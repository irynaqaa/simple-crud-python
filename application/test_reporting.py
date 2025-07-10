import pytest
from reporting import Reporting
from transaction_management import Transaction


def test_reporting_init():
    transactions = [Transaction('2022-01-01', 100.0, 'Food', 'Lunch'), Transaction('2022-01-02', 200.0, 'Transportation', 'Gas')]
    reporting = Reporting(transactions)
    assert reporting.transactions == transactions


def test_reporting_generate_report():
    transactions = [Transaction('2022-01-01', 100.0, 'Food', 'Lunch'), Transaction('2022-01-02', 200.0, 'Transportation', 'Gas')]
    reporting = Reporting(transactions)
    reporting.generate_report()
    # Check if the report is generated correctly
