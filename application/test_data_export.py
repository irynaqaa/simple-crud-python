import pytest
from data_export import DataExport
from transaction_management import Transaction
import os
import csv


def test_data_export_init():
    transactions = [Transaction('2022-01-01', 100.0, 'Food', 'Lunch'), Transaction('2022-01-02', 200.0, 'Transportation', 'Gas')]
    data_export = DataExport(transactions)
    assert data_export.transactions == transactions


def test_data_export_export_to_csv():
    transactions = [Transaction('2022-01-01', 100.0, 'Food', 'Lunch'), Transaction('2022-01-02', 200.0, 'Transportation', 'Gas')]
    data_export = DataExport(transactions)
    filename = 'transactions.csv'
    data_export.export_to_csv(filename)
    assert os.path.exists(filename)
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header
        for i, row in enumerate(reader):
            if i == 0:
                assert row == ['2022-01-01', '100.0', 'Food', 'Lunch']
            elif i == 1:
                assert row == ['2022-01-02', '200.0', 'Transportation', 'Gas']
