import urllib
from Command import Command
from Help import Help
from GlobalVariables import goodReadsUrl, listOfCommands


def mainControlFlow():
    while True:
        temp = None
        currCommand = input("What command would you like to execute?\n")
        if currCommand == 'help':
            temp = Help(currCommand)
            temp.execute()
        elif currCommand == 'listGenres':

        else:
            print("Command not recognized, please type help for more information.")

mainControlFlow()
