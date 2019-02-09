# Lays the structural foundation of the behaviour of a command.
from abc import ABC, abstractmethod

class Command(ABC):

    def __init__(self, commandName):
        self.commandName = commandName

    def commandType(self):
        return self.commandName

    @abstractmethod
    def execute(self):
        pass
