from Command import Command

class Add(Command):
    listToRead = []
    listCurrRead = []
    def execute(self, argOne, argTwo):
        if (argOne == 'toRead'):
            Add.listToRead.append(argTwo)
        elif argTwo == 'currentlyReading':
            Add.listCurrRead.append(argTwo)