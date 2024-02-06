"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self,filename):
        self.filename = open(filename, "r")
        self.lines=self.filename.readlines()

    def getReadWords(self):
        count = 0        
            
        return print(str(len(self.lines)) + " words read" )
    def random(self):
        length = len(self.lines)
        randomNum= random.randint(0, length)
        return print(self.lines[randomNum])
words= WordFinder("words.txt") 
words.getReadWords()
words.random()

