from Command import Command

from GlobalVariables import *

class Genre(Command):
    # Accepts a httpaddress and returns the contents of the webpage as a string,
    # and prints it to the command line.
    def openWebpage(httpAddress):
        contents = urllib.urlOpen(httpAddress).read()
        print(contents)
        return contents

    # Queries a specific genre and returns contents of that webpages genre as a string,
    # and prints it to the command line.
    def queryGenre(genre):
        contents = urllib.urlOpen(goodReadsUrl + "/genre/" + genre)
        print(contents)
        return contents

    def queryMostRead(genre):
        contents = urllib.urlOpen(goodReadsUrl + "/genre/most_read/" + genre)
        print(contents)
        return contents

    def execute(self, genre):

