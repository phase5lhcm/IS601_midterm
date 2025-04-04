"""Inheirits from the Command base class to implement the multiplication operation via the execute method"""

import logging as log

from calculator.commands.command import Command


class MultiplyCommand(Command):
    def __init__(self, first_operand, second_operand):
        self.first_operand = first_operand
        self.second_operand = second_operand

    def execute(self):
        log.info("Running multiplication operation")
        return self.first_operand * self.second_operand
