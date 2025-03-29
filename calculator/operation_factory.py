from calculator.commands.add import AddCommand
from calculator.commands.divide import DivideCommand
from calculator.commands.multiply import MultiplyCommand
from calculator.commands.subtract import SubtractCommand
from calculator.strategy.average import AverageOperation
from calculator.strategy.power import PowerOperation


class OperationFactory:
    """Factory that creates instances of each arithmetic operation when user specifies from menu"""

    @staticmethod
    def get_operation(command, a, b):
        commands = {
            "ADD": AddCommand,
            "SUBTRACT": SubtractCommand,
            "MULTIPLY": MultiplyCommand,
            "DIVIDE": DivideCommand,
            "POWER": PowerOperation,
            "AVERAGE": AverageOperation,
        }
        command = command.upper()
        if command not in commands:
            return None
        return commands[command](a, b)
