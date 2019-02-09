# Deals with logic pertaining to the help command.
from Command import Command
from GlobalVariables import *

class Help(Command):
    def execute(self):
        print("List of possible commands:")
        for i in range(0, len(listOfCommands)):
            print("%s" %(listOfCommands[i]))

