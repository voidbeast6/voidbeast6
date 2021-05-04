#
#created by Lewis
#finished on 3rd May 2021
#

import tkinter as tk
import random, string

class MultipleChoice(tk.Tk):
    def __init__(self, *args, file = "words.txt"):
        tk.Tk.__init__(self, *args)
        self.width=800
        self.height=600
        self.geometry(str(self.width)+"x"+str(self.height))

#create the variables
        self.score = tk.IntVar(self)
        self.pos = tk.StringVar(self)
        self.definition = tk.StringVar(self)
        self.answer = tk.StringVar(self)
        self.wrongChoice1 = tk.StringVar(self)
        self.wrongChoice2 = tk.StringVar(self)
        self.wrongChoice3 = tk.StringVar(self)
        
        
#create the top container which contains menu, score and hint informations
        topWindow = tk.Frame(master = self, relief = tk.RAISED)
        topWindow.pack(side = "top", fill = "x", expand = True)
        self.menuButton = tk.Button(master = topWindow, text = "Menu", font = 50, pady=5, state = "disabled", command = self.gameMenu)
        self.menuButton.pack(side = "right")
        scoreBoard = tk.Label(master = topWindow, text = " Your score: ", font = 50)
        scoreBoard.pack(side = "left", fill = "y")
        scoreText = tk.Label(master = topWindow, textvariable = self.score, font = 50)
        scoreText.pack(side = "left", fill = "y")
        self.posText = tk.Label(master = topWindow, textvariable = self.pos, font = 50)
        self.posText.pack_forget()
        
#Buttons area
        bottomWindow = tk.Frame(master = self, relief = tk.RAISED, borderwidth = 1)
        bottomWindow.pack(side = "bottom", fill = "x", expand = True)
        buttonLeft = tk.Frame(master = bottomWindow, relief = tk.RAISED, borderwidth = 1)
        buttonRight = tk.Frame(master = bottomWindow, relief = tk.RAISED, borderwidth = 1)
        buttonLeft.pack(side = "left", fill = 'y', expand = True)
        buttonRight.pack(side = "right", fill = 'y', expand = True)
        self.button1 = tk.Frame(master = buttonLeft, relief = tk.RAISED, borderwidth = 1)
        self.button1.pack(fill = 'both', expand = True)
        self.button2 = tk.Frame(master = buttonLeft, relief = tk.RAISED, borderwidth = 1)
        self.button2.pack(fill = 'both', expand = True)
        self.button3 = tk.Frame(master = buttonRight, relief = tk.RAISED, borderwidth = 1)
        self.button3.pack(fill = 'both', expand = True)
        self.button4 = tk.Frame(master = buttonRight, relief = tk.RAISED, borderwidth = 1)
        self.button4.pack(fill = 'both', expand = True)
        self.message = tk.Label(master = bottomWindow, text = "3 out of 4 buttons are wrong answers", font = 30)
        self.message.pack(side = "top", fill = 'both', expand = True)

#create the center window to contain the word
        self.wordWindow = tk.Frame(master = self)
        self.wordWindow.pack(fill='both', expand = True)
        self.definitionText = tk.Label(master = self.wordWindow, textvariable = self.definition, font = 100)
        self.definitionText.pack_forget()
        self.starting = tk.Button(master = self.wordWindow, text = "click to start", font = 50, command = self.start)
        self.starting.pack(fill='both', expand = True)

#pick the word list
        words=list()
        with open(file, "r") as infile:
            count=0
            for line in infile:
                count +=1
#skip the first line
                if count == 1:
                    continue
#create a list whose elements are [word,category,meaning]
                words.append(line.strip().split(';'))
        self.wordList = list()
        self.category = dict()
        self.meaning = dict()
        for x in words:
            word=x[0]
            self.wordList.append(word.lstrip().casefold())
            self.category[word]=x[1].lstrip().casefold()
            self.meaning[word]=x[2].lstrip().casefold()

#start game and show the buttons and hints
    def start(self):
        self.message.destroy()
        self.starting.destroy()
        self.definitionText.pack(fill='both', expand = True)
        self.posText.pack(fill = "y", expand = True)
        self.menuButton.config(state = "normal")
        self.next()

#switch to next word
    def next(self):
#Random position for the buttons
        positions=[self.button1, self.button2, self.button3, self.button4]
        position1=random.choice(positions)
        positions.remove(position1)
        position2=random.choice(positions)
        positions.remove(position2)
        position3=random.choice(positions)
        positions.remove(position3)
        position4=positions[0]
        self.right = tk.Button(master = position1, textvariable = self.answer, font = 30, padx=self.width/6, pady=5, command = self.getScore)
        self.wrong1 = tk.Button(master = position2, textvariable = self.wrongChoice1, font = 30, padx=self.width/6, pady=5, command = self.wrongAnswer)
        self.wrong2 = tk.Button(master = position3, textvariable = self.wrongChoice2, font = 30, padx=self.width/6, pady=5, command = self.wrongAnswer)
        self.wrong3 = tk.Button(master = position4, textvariable = self.wrongChoice3, font = 30, padx=self.width/6, pady=5, command = self.wrongAnswer)
        self.right.pack(fill='both', expand = True)
        self.wrong1.pack(fill='both', expand = True)
        self.wrong2.pack(fill='both', expand = True)
        self.wrong3.pack(fill='both', expand = True)

#pick the word randomly and set the hints to the boxes
        word = random.choice(self.wordList)
        self.pos.set(self.category[word])
        
#set that 40 is the maximum length of a line
        self.definition.set(self.cutByLength(self.meaning[word], 40))
        self.answer.set(word)
        
#change the word random times
        while True:
            for n1 in range(random.randint(1, len(word)*4)):
                word1 = self.changeIndex(word, random.randint(0,len(word)-1))
                word1 = self.changeAlphabet(word, word[random.randint(0,len(word)-1)])
            if word1 != word:
                break
        while True:
            for n2 in range(random.randint(1, len(word)*4)):
                word2 = self.changeIndex(word, random.randint(0,len(word)-1))
                word2 = self.changeAlphabet(word, word[random.randint(0,len(word)-1)])
            if word2 != word and word2 != word1:
                break
        while True:
            for n3 in range(random.randint(1, len(word)*4)):
                word3 = self.changeIndex(word, random.randint(0,len(word)-1))
                word3 = self.changeAlphabet(word, word[random.randint(0,len(word)-1)])
            if word3 != word and word3 != word1 and word3 != word2:
                break
        self.wrongChoice1.set(word1)
        self.wrongChoice2.set(word2)
        self.wrongChoice3.set(word3)

#cut the sentence by max length
    def cutByLength(self, sentence, maxLength):
        list = sentence.split()
        l = 0
        sentence = ""
        for n in list:
            l += len(n)
            if l <maxLength:
                sentence = sentence + n + " "
            else:
                sentence = sentence + "\n" + n + " "
                l=0
        return sentence

#change the word by replace specific index
    def changeIndex(self, word, index):
        alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        newWord = list(word)
        newWord[index] = random.choice(alphabets)
        newWord = "".join(newWord)
        return newWord

#change the word by replace specific alphabet
    def changeAlphabet(self, word, alphabet):
        alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        alphabets.remove(alphabet)
        wrong = random.choice(alphabets)
        newWord = word.replace(alphabet,wrong)
        return newWord

    def wrongAnswer(self):
        self.score.set(self.score.get()-1)
        self.right.destroy()
        self.wrong1.destroy()
        self.wrong2.destroy()
        self.wrong3.destroy()
        self.next()

    def getScore(self):
        self.score.set(self.score.get()+1)
        self.right.destroy()
        self.wrong1.destroy()
        self.wrong2.destroy()
        self.wrong3.destroy()
        self.next()

#create menu to show quit button and resume button, hints and guess buttons would be hidden
    def gameMenu(self):
        self.menuButton.config(state = "disabled")
        self.posText.pack_forget()
        self.definitionText.pack_forget()
        self.right.pack_forget()
        self.wrong1.pack_forget()
        self.wrong2.pack_forget()
        self.wrong3.pack_forget()
        self.buttonResume = tk.Button(self.wordWindow, text = "Resume", font = 50, padx=self.width/5, pady=self.height/50, command=self.resume)
        self.buttonQuit = tk.Button(self.wordWindow, text = "Exit", font = 50, padx=self.width/5, pady=self.height/50,command=self.destruct)
        self.buttonResume.pack()
        self.buttonQuit.pack()

#destroy the menu and show the hints and guess buttons again
    def resume(self):
        self.menuButton.config(state = "normal")
        self.buttonResume.destroy()
        self.buttonQuit.destroy()
        self.definitionText.pack()
        self.posText.pack(fill = "y", expand = True)
        self.right.pack(fill='both', expand = True)
        self.wrong1.pack(fill='both', expand = True)
        self.wrong2.pack(fill='both', expand = True)
        self.wrong3.pack(fill='both', expand = True)

    def destruct(self):
        self.destroy()
    
def MCgame():
    game = MultipleChoice()
    game.mainloop()

if __name__ == '__main__':
    game = MultipleChoice()
    game.mainloop()
    
