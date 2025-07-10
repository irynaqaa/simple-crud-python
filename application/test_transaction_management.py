import pytest
from transaction_management import Transaction


def test_transaction_init():
    transaction = Transaction('2022-01-01', 100.0, 'Food', 'Lunch')
    assert transaction.date == '2022-01-01'
    assert transaction.amount == 100.0
    assert transaction.category == 'Food'
    assert transaction.description == 'Lunch'
