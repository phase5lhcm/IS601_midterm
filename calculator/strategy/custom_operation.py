"""Like the Command class, this is a base class for custom operations (our plugins)"""
from abc import ABC, abstractmethod


class CustomCommand(ABC):
    """A base class for the plugins"""
    @abstractmethod
    def execute(self, a, b):
        pass