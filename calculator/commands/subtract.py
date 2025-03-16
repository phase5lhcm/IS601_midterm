#Inheirits from the Command base class to implement the subtraction operation via the execute method
from .commands import Command
from ..utils.validator import Validator
import logging as log

class SubtractCommand(Command):
    def __init__(self, first_operand, second_operand):
        self.first_operand = first_operand
        self.second_operand = second_operand
    
    def execute(self):
        log.info("Running subtraction operation")
        Validator.validate(self.first_operand, "Value must be greater than zero")
        return self.first_operand - self.second_operand