import pytest
from faker import Faker
from calculator.calculator import CalculatorFacade

faker = Faker()

def test_calculator_facade():
    calculator = CalculatorFacade()
    a, b = faker.random_int(min=1, max=100), faker.random_int(min=1, max=100)
    result = calculator.calculate("ADD", a, b)
    assert result == a + b
