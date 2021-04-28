import tkinter as tk
import string
from wordbank import *

class dictGUI(tk.Tk):
    def __init__(self, filename):
        tk.Tk.__init__(self)
        self.geometry("800x600")
        self.title("Dictionary")
        
        self.config(background="yellow")
        wordbank= WordBank(filename)
        wordlist= wordbank.wordList
        buttons=list()
        for n in range(len(wordlist)):
            rowindex=0
            columnindex=0
            buttons.append(tk.Button(self,text=str(n)+'.'+wordlist[n],row=rowindex,column=columnindex,padx=20,fg="blue",bg="yellow",command=self.viewer(wordlist[n])).grid(row=rowindex,column=columnindex))
            
            rowindex+=1
            columnindex+=1
            if row>20:
                row-=20
                column+=1
        
    def viewer(self, word):
        self.wordWindow = tk.Toplevel()
        self.category = Label(wordWindow,text=wordbank.category[word])
        self.meaning = Label(wordWindow,text=wordbank.meaning[word])
        category.pack()
        meaning.pack()
    
    

    

if __name__ == "__main__":

    dictionary = dictGUI("words.txt")
