#Inheirits from the Command base class to implement the multiplication operation via the execute method
from calculator.commands.command import Command
import logging as log

class MultiplyCommand(Command):
    def __init__(self, first_operand, second_operand):
        self.first_operand = first_operand
        self.second_operand = second_operand
    
    def execute(self):
        log.info("Running multiplication operation")
        return self.first_operand * self.second_operand