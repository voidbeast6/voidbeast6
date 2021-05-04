import tkinter as tk
from nltk.corpus import wordnet

class WordDefinition(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.width=800
        self.height=600
        self.geometry(str(self.width)+"x"+str(self.height))
        
        self.history = tk.StringVar(self)
        self.definition = tk.StringVar(self)
        
        topWindow = tk.Frame(master = self)
        topWindow.pack(side = "top", fill = "x", expand = True)

        self.slogan = tk.Label(master = topWindow, text = "Seach the definition", font = 50)
        self.slogan.pack()
        
        self.searchWord = tk.Entry(master = topWindow,bd = 20)
        self.searchWord.pack()
        
        self.searchButton = tk.Button(master = topWindow, text = "Click to search", font = 100, command = self.search)
        self.searchButton.pack()
        
        self.quit = tk.Button(master = topWindow, text = "Exit", font = 50, command = self.destruct)
        self.quit.pack()
        
        bottomWindow = tk.Frame(master = self, highlightbackground="black", highlightthickness=1)
        bottomWindow.pack(side = "bottom", fill = "x")

        historyContainer = tk.Frame(master = bottomWindow, relief = tk.RAISED, highlightbackground="black", highlightthickness=1)
        historyContainer.pack(side = "left", fill = "y")

        historyLabel = tk.Label(master = historyContainer, text = "Search History", font = 50, highlightbackground="black", highlightthickness=0.1)
        historyLabel.pack(side = "top", fill = "x")
        
        self.searchHistory = tk.Label(master = historyContainer, textvariable = self.history, font = 20)
        self.searchHistory.pack(side = "top", fill = "y")

        definitionContainer = tk.Frame(master = bottomWindow)
        definitionContainer.pack(fill = "both")

        definitionLabel = tk.Label(master = definitionContainer, text = "definition", font = 50)
        definitionLabel.pack(side = "top", fill = "x")

        self.definitionBox = tk.Label(master = definitionContainer, textvariable = self.definition, font = 20)
        self.definitionBox.pack(fill = "both")

        self.record = list()
                

    def search(self):
        word = self.searchWord.get()
        self.record.insert(0,word)
        l=0
        list=""
        for w in self.record:
            l+=len(w)
            list=list+w+'\n'
            if l>20:
                break
        self.history.set(list)
        print(list)
        syns = wordnet.synsets(word)
        meaning = syns[0].definition()
        self.definition.set(meaning)
    
    def destruct(self):
        self.destroy()
def worddefine():
    define = WordDefinition()
    define.mainloop()
