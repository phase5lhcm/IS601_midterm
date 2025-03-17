#Inheirits from the Command base class to implement the addition operation via the execute method
from calculator.commands.command import Command
import logging as log

class AddCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def execute(self):
        log.info("Running addition operation")
        return self.a + self.b