from calculator.strategy.custom_operation import CustomOperation
from ..utils.validator import Validator

class PowerOperation(CustomOperation):
    """Raises a number to the power of another."""
    
    def execute(self, a, b):
        if self.a == 0 and b == 0:
            Validator.validate(a, "Value must be greater than zero")
        return a ** b
