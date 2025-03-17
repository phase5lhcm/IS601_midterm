#Inheirits from the Command base class to implement the division operation via the execute method
from calculator.commands.command import Command
from ..utils.validator import Validator
import logging as log


class DivideCommand(Command):
    def __init__(self, first_operand, second_operand):
        self.first_operand = first_operand
        self.second_operand = second_operand
    
    def execute(self):
        log.info("Running division operation")
        Validator.validate(self.second_operand,"Cannot divide by zero" )
        return self.first_operand / self.second_operand