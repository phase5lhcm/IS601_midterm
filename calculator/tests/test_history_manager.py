import pytest
from faker import Faker
from calculator.history_manager import HistoryManager

faker = Faker()

def test_history_manager():
    history = HistoryManager()
    a, b = faker.random_int(min=1, max=100), faker.random_int(min=1, max=100)
    history.add_record("ADD", a, b, a + b)
    assert not history.history.empty
