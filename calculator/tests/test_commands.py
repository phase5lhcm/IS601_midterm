import pytest
from faker import Faker
from calculator.commands.add import AddCommand
from calculator.commands.subtract import SubtractCommand
from calculator.commands.multiply import MultiplyCommand
from calculator.commands.divide import DivideCommand

# Initialize Faker
fake = Faker()

# Use parametrize to generate more than one test cases
@pytest.mark.parametrize("a, b, expected", [
    (a, b, a + b) 
    for a, b in [(fake.random_int(min=-100, max=100), fake.random_int(min=-100, max=100)) for _ in range(5)]
])
def test_add_command(a,b,expected):
    command = AddCommand(a, b)
    assert command.execute() == expected 

# @pytest.mark.parametrize("a, b, expected", [
#     (fake.random_int(min=-100, max=100), fake.random_int(min=-100, max=100), lambda a, b: a - b)
#     for _ in range(5)  
# ])
# def test_subtract_command(a, b, expected):
#     command = SubtractCommand(a, b, expected)
#     assert command.execute() == a - b

# pytest.mark.parametrize("a, b, expected", [
#     (fake.random_int(min=-10, max=10), fake.random_int(min=-10, max=10), lambda a, b: a * b)
#     for _ in range(5)
# ])
# def test_multiply_command(a, b, expected):
#     command = MultiplyCommand(a, b, expected)
#     assert command.execute() == a * b

# @pytest.mark.parametrize("a, b, expected", [
#     (fake.random_int(min=1, max=100), fake.random_int(min=1, max=10), lambda a, b: a / b)
#     for _ in range(5)
# ])
# def test_divide_command(a, b, expected):
#     command = DivideCommand(a, b, expected)
#     assert command.execute() == a / b

# def test_divide_by_zero():
#     command = DivideCommand(5, 0)
#     assert command.execute() == "Error: Division by zero"
