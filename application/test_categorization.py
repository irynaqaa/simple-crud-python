import pytest
from categorization import Category
from transaction_management import Transaction


def test_category_init():
    category = Category('Food')
    assert category.name == 'Food'
    assert category.transactions == []


def test_category_add_transaction():
    category = Category('Food')
    transaction = Transaction('2022-01-01', 100.0, 'Food', 'Lunch')
    category.add_transaction(transaction)
    assert len(category.transactions) == 1
    assert category.transactions[0].date == '2022-01-01'
    assert category.transactions[0].amount == 100.0
    assert category.transactions[0].category == 'Food'
    assert category.transactions[0].description == 'Lunch'
