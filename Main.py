import urllib2
goodReadsUrl = "https://www.goodreads.com"

listOfCommands = ['help']

# Accepts a httpaddress and returns the contents of the webpage as a string,
# and prints it to the command line.
def openWebpage(httpAddress):
    contents = urllib2.urlOpen(httpAddress).read()
    print(contents)
    return contents

# Queries a specific genre and returns contents of that webpages genre as a string,
# and prints it to the command line.
def queryGenre(genre):
    contents = urllib2.urlOpen(goodReadsUrl + "/genre/" + genre)
    print(contents)
    return contents

def queryMostRead(genre):
    contents = urllib2.urlOpen(goodReadsUrl + "/genre/most_read/" + genre)
    print(contents)
    return contents

def mainControlFlow():
    while True:
        currCommand = input("What command would you like to execute?")

mainControlFlow()
