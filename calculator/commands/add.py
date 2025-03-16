#Inheirits from the Command base class to implement the addition operation via the execute method
from .commands import Command

class AddCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def execute(self):
        return self.a + self.b