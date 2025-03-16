from commands.add import AddCommand
from commands.subtract import SubtractCommand
from commands.multiply import MultiplyCommand
from commands.divide import DivideCommand

class OperationFactory:
    """Factory that creates instances of each arithmetic operation when user specifies from menu"""

    @staticmethod
    def get_command(command, a, b):
        commands = {
            "Add": AddCommand,
            "Subtract": SubtractCommand,
            "Multiply": MultiplyCommand,
            "Divide": DivideCommand
        }
        if(command.upper in commands):
             return commands[command.upper()](a, b)
        return None
    
