import pytest
from faker import Faker

from calculator.strategy.power import PowerOperation

# Initialize Faker
fake = Faker()


def test_power_operation():
    a, b = fake.random_int(min=1, max=10), fake.random_int(min=1, max=5)
    power = PowerOperation()
    assert power.execute(a, b) == a**b


def test_power_operation_zero():
    power = PowerOperation()
    with pytest.raises(Exception):
        power.execute(0, 0)
