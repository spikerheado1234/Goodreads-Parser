# Deals with logic pertaining to the help command.
from Main.py import goodReadsUrl, listOfCommands

def help():
    print("List of possible commands: \n")
    for i in range(0, len(listOfCommands)):
        print("%s\n" %(listOfCommands[i]))
