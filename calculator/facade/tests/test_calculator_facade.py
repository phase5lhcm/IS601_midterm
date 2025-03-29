from unittest.mock import MagicMock

import pytest
from faker import Faker

from calculator.facade.calculator import CalculatorFacade

faker = Faker()


@pytest.fixture
def calculator_facade():
    """Fixture to ensure there is an instance of CalculatorFacade for testing"""
    return CalculatorFacade()


def test_calculator_operations(calculator_facade):
    assert calculator_facade.calculate("add", 2, 3) == 5
    assert calculator_facade.calculate("subtract", 10, 2) == 8
    assert calculator_facade.calculate("multiply", 4, 5) == 20
    assert calculator_facade.calculate("divide", 8, 2) == 4


def test_handle_invalid_operation(calculator_facade, capsys):
    """Ensures appropriate response for invalid operation"""
    assert (
        calculator_facade.calculate("invalid operation", 10, 2) == "Invalid Operation"
    )


def test_show_history(calculator_facade, capsys):
    """Mocked test to perform show_history method"""
    calculator_facade.history_manager.display_history = (
        MagicMock()
    )  # Mocks the method call
    calculator_facade.show_history()  # Now we can call the method without actually affectibg the actual csv file

    # Only assert that the call was made. Unable to assert the actual repsonse since I am mocking the call
    calculator_facade.history_manager.display_history.assert_called_once()


def test_delete_history(calculator_facade):
    """Test delete_history method"""
    # Mock the delete_history method
    calculator_facade.history_manager.delete_history = MagicMock()

    # Call the method
    calculator_facade.delete_history()

    # Verify it was called once
    calculator_facade.history_manager.delete_history.assert_called_once()
