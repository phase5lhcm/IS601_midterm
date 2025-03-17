import pytest
from faker import Faker
from calculator.operation_factory import OperationFactory
from calculator.commands.add import AddCommand
from calculator.commands.subtract import SubtractCommand
from calculator.commands.multiply import MultiplyCommand
from calculator.commands.divide import DivideCommand

faker = Faker()

@pytest.mark.parametrize("operation, command_class, func", [
    ("ADD", AddCommand, lambda a, b: a + b),
    ("SUBTRACT", SubtractCommand, lambda a, b: a - b),
    ("MULTIPLY", MultiplyCommand, lambda a, b: a * b),
    ("DIVIDE", DivideCommand, lambda a, b: a / b if b != 0 else None)
])
@pytest.mark.parametrize("a, b", [(faker.random_int(min=-100, max=100), faker.random_int(min=-100, max=100)) for _ in range(5)])
def test_factory_operations(operation, command_class, func, a, b):
    if operation == "DIVIDE" and b == 0:
        b = 1  # Avoid division by zero error in test cases
    
    operation_instance = OperationFactory.get_operation(operation, a, b)
    assert isinstance(operation_instance, command_class)
    assert operation_instance.execute() == func(a, b)

@pytest.mark.parametrize("a", [faker.random_int(min=-100, max=100) for _ in range(5)])
def test_factory_divide_by_zero(a):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        operation = OperationFactory.get_operation("DIVIDE", a, 0)
        operation.execute()
