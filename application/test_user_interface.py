import pytest
from user_interface import UserInterface
import tkinter as tk


def test_user_interface_init():
    root = tk.Tk()
    user_interface = UserInterface(root)
    assert user_interface.root == root
    assert user_interface.transactions == []
    assert user_interface.categories == []
