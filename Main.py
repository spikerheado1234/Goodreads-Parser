import urllib
from Command import Command
from Help import Help
from GlobalVariables import goodReadsUrl, listOfCommands
from Genre import Genre

def mainControlFlow():
    while True:
        temp = None
        currCommand = []
        for i in input("Please input a command: \n").split():
            currCommand.append(i)
        if currCommand[0] == 'help':
            temp = Help(currCommand[0])
            temp.execute()
        elif currCommand[0] == 'listGenre':
            temp = Genre(currCommand[0])
            temp.execute(currCommand[1])
        else:
            print("Command not recognized, please type help for more information.")

mainControlFlow()
