import string, random

class WordBank():

    def __init__(self, filename):
        self.words=list()
        with open(filename, "r") as infile:
            count=0
            for line in infile:
                count +=1
                #skip the first line
                if count == 1:
                    continue
                #create a list whose elements are [word,category,meaning]
                self.words.append(line.strip().split(';'))
        self.wordList=list()
        self.category=dict()
        self.meaning=dict()
        for x in self.words:
            word=x[0]
            self.wordList.append(word)
            self.category[word]=x[1]
            self.meaning[word]=x[2]
        
    def pickWord(self, minLen=0):
        # randomly choose a word
        while True:
            word = random.choice(self.wordList)
            if len(word) >= minLen:
                break
        # create a list of the same length as the word
        # but contains dashes '-'
        return (word)

    def getHint(self, word):
        hint = self.category[word] + "\n" + self.meaning[word]
        return hint

if __name__ == "__main__":
    wordBank = WordBank("words.txt")
    print(wordBank.wordList)
    print(wordBank.category)
    print(wordBank.meaning)
    print(wordBank.pickWord())
