from Command import Command
from GlobalVariables import *
import urllib.request
from bs4 import BeautifulSoup

class Genre(Command):
    def execute(self, genre):
        listOfTopBooks = []
        contents = urllib.request.urlopen(goodReadsUrl + "/genres/most_read/" + genre)
        page_content = BeautifulSoup(contents.read(), "html.parser")
        for div in page_content.find_all('div', attrs={'class': 'bigBoxBody'}):
            for divTwo in div.find_all('div', attrs={'class': 'bigBoxContent'}):
                for divThree in divTwo.find_all('div', attrs={'class': 'coverRow'}):
                    for divFour in divThree.find_all('div', attrs={'class': 'leftAlignedImage bookBox'}):
                        for divFive in divFour.find_all('div', attrs={'class': 'coverWrapper'}):
                            for divSix in divFive.find_all('a'):
                                listOfTopBooks.append(divSix.img['alt'])
        
        for i in range(0, min(len(listOfTopBooks), 10)):
            print(listOfTopBooks[i])
