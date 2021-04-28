import tkinter as tk
import random, time, string, sys
from wordbank import *
sys.setrecursionlimit(1700)
class gameGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("800x600")

        self.timeLeft = 180# in second

        self.topWindow = tk.Frame(master = self, relief = tk.RAISED).pack(side = "top", fill = "x", expand = True)
        self.timerArea = tk.Frame(master = self.topWindow, borderwidth = 1).pack(side = "right")
        self.scoreArea = tk.Frame(master = self.topWindow, borderwidth = 1).pack(side = "left")
        self.hintArea = tk.Frame(master = self.topWindow, borderwidth = 1).pack(side = "bottom")
        self.timer = tk.Button(master = self.timerArea, text = str(self.timeLeft), command = self.menu).pack()
        self.hint = tk.Label(master = self.hintArea, text = "hint").pack(side = "bottom")
        self.score = tk.Label(master = self.scoreArea, text = "score").pack(fill='both')

        self.wordWindow = tk.Frame(master = self).pack()
        self.word = tk.Label(master = self.wordWindow, text = "word").pack()

        
        #Bottom buttons area
        self.bottomWindow = tk.Frame(master = self, relief = tk.RAISED, borderwidth = 1).pack(side = "bottom", fill = "x")
        self.buttonLeft = tk.Frame(master = self.bottomWindow, relief = tk.RAISED, borderwidth = 1).pack(side = "left", fill = 'both', expand = True)
        self.buttonRight = tk.Frame(master = self.bottomWindow, relief = tk.RAISED, borderwidth = 1).pack(side = "right", fill = 'both', expand = True)
        self.button1 = tk.Frame(master = self.buttonLeft, relief = tk.RAISED, borderwidth = 1).pack(fill = "x", expand = True)
        self.button2 = tk.Frame(master = self.buttonLeft, relief = tk.RAISED, borderwidth = 1).pack(fill = "x", expand = True)
        self.button3 = tk.Frame(master = self.buttonRight, relief = tk.RAISED, borderwidth = 1).pack(fill = "x", expand = True)
        self.button4 = tk.Frame(master = self.buttonRight, relief = tk.RAISED, borderwidth = 1).pack(fill = "x", expand = True)

        #Random position
        position=[self.button1, self.button2, self.button3, self.button4]
        position1=position[random.randint(0,3)]
        position.remove(position1)
        position2=position[random.randint(0,2)]
        position.remove(position2)
        position3=position[random.randint(0,1)]
        position.remove(position3)
        position4=position[0]
    
        self.right = tk.Button(master = position1, text = "a", pady=5).pack(fill='both', expand = True)
        self.wrong1 = tk.Button(master = position2, text = "b", pady=5, command = self.wrong(self.wrong1)).pack(fill='both', expand = True)
        self.wrong2 = tk.Button(master = position3, text = "c", pady=5, command = self.wrong(self.wrong2)).pack(fill='both', expand = True)
        self.wrong3 = tk.Button(master = position4, text = "d", pady=5, command = self.wrong(self.wrong3)).pack(fill='both', expand = True)
        

    def changeWord(self, word, hint):
        self.word.config(text=word)
        self.hint.config(text=hint)

    def changeAlphabet(self, alphabet):
        self.right.config(text=alphabet)
        alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        alphabets.remove(alphabet)
        b=alphabets[random.randint(0,24)]
        self.wrong1.config(text = b)
        alphabets.remove(b)
        c=alphabets[random.randint(0,23)]
        self.wrong2.config(text =c )
        alphabets.remove(c)
        d=alphabets[random.randint(0,22)]
        self.wrong3.config(text = d)
    
    def menu(self):
        self.menu = tk.Toplevel()
        self.buttonResume = tk.Button(self.menu, text = "Resume",command=self.menu.destroy()).pack()
        self.buttonQuit = tk.Button(self.menu , text = "Exit",command=self.window.destroy()).pack()
        
    def wrong(self, button):
        self.timeLeft -=5
        self.button['state'] = tk.DISABLED

    #def correct(self):
        




if __name__ == "__main__":
    test=gameGUI()
    test.mainloop()
    
    







