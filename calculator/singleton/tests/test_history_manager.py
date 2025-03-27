import os

import pytest
from faker import Faker

from calculator.singleton.history_manager import HistoryManager

faker = Faker()


def history_manager():
    """Creates a single instance of the history manager"""
    history_manager = HistoryManager()
    yield history_manager


if os.path.exists(history_manager.USER_HISTORY):
    os.remove(history_manager.USER_HISTORY)


def add_record_test():
    """Test to add records to the history file"""
    history = HistoryManager()
    a, b = faker.random_int(min=1, max=100), faker.random_int(min=1, max=100)
    history.add_record("ADD", a, b, a + b)
    assert not history.history.empty


def delete_history_file_test(history_manager):
    # First, create a file to delete
    history_manager.recreate_file
    history_manager.delete_history()
    assert not os.path.exists(history_manager.USER_HISTORY)
