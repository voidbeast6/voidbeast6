from nltk.corpus import wordnet
from word_list import WordList

synonyms = []
antonyms = []
def findsynonmy(word):
    for syn in wordnet.synsets(word):
	    for l in syn.lemmas():
		    synonyms.append(l.name())
		    if l.antonyms():
			     antonyms.append(l.antonyms()[0].name())


    

if __name__ == "__main__":
    rand = WordList.pickWord(WordList("dict.txt"))
    findsynonmy(rand[0])
    print(set(synonyms))
    print(set(antonyms))
