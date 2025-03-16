import pytest
from faker import Faker
from commands.add import AddCommand
from commands.subtract import SubtractCommand
from commands.multiply import MultiplyCommand
from commands.divide import DivideCommand

# Initialize Faker
fake = Faker()

def test_add_command():
    a, b = fake.random_int(min=1, max=100), fake.random_int(min=1, max=100)
    command = AddCommand(a, b)
    assert command.execute() == a + b

def test_subtract_command():
    a, b = fake.random_int(min=1, max=100), fake.random_int(min=1, max=100)
    command = SubtractCommand(a, b)
    assert command.execute() == a - b

def test_multiply_command():
    a, b = fake.random_int(min=1, max=100), fake.random_int(min=1, max=100)
    command = MultiplyCommand(a, b)
    assert command.execute() == a * b

def test_divide_command():
    a, b = fake.random_int(min=1, max=100), fake.random_int(min=1, max=100)
    command = DivideCommand(a, b)
    assert command.execute() == a / b

def test_divide_by_zero():
    a = fake.random_int(min=1, max=100)
    command = DivideCommand(a, 0)
    assert command.execute() == "Error: Division by zero"
