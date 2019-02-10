import urllib
from Command import Command
from Help import Help
from GlobalVariables import goodReadsUrl, listOfCommands
from Add import Add
from List import List

def mainControlFlow():
    while True:
        temp = None
        currCommand = []
        for i in input("Please input a command: \n").split():
            currCommand.append(i)
        if currCommand[0] == 'help':
            temp = Help(currCommand[0])
            temp.execute()
        elif currCommand[0] == 'add':
            if currCommand[1] == 'toRead':
                temp = Add(currCommand[0])
                temp.execute(currCommand[1], currCommand[2])
            elif currCommand[1] == 'currentlyReading':
                temp = Add(currCommand[0])
                temp.execute(currCommand[1], currCommand[2])
            else:
                print("Command not recognized, please type help for more information.")
        elif currCommand[0] == 'list':
            if currCommand[1] == 'genre':
                temp = List(currCommand[0] + currCommand[1])
                temp.execute(currCommand[2])
            elif currCommand[1] == 'toRead':
                temp = List(currCommand[0] + currCommand[1])
                temp.execute(currCommand[1])
            elif currCommand[1] == 'currentlyReading':
                temp = List(currCommand[0] + currCommand[1])
                temp.execute(currCommand[1])
        else:
            print("Command not recognized, please type help for more information.")

mainControlFlow()