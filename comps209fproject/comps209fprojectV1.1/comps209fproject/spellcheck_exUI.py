import tkinter as tk
from spellcheck_ex import *
  

def spellcheck():
    window = tk.Tk()  
    label = tk.Label(window,
    text="Thank you for using spell checker",
    foreground="green", #set text color to green
    background="yellow" #set the background to black
    ).pack()
    Label2 = Label(window, text="input a file for check spelling").pack()
    filegetVar= StringVar()
    
    filegetEntry = Entry(window, textvariable=filegetVar).pack()  
    
    button = tk.Button(window,text="Click here to start the spell check!",command =lambda: checkspelling(filegetVar.get()),
    width=28,
    height=7,
    bg="black",
    fg="green",
    ).pack()
    quitButton = Button(window, text="back to menu", command=lambda : window.destroy() ).pack()
    Correcttxt = Text(window)
    
    def checkspelling(filename):
        print(filename)
        
        with open(filename, "r",encoding="utf-8") as f:        # Opening the test file with the intention to read
            text = f.read()                     # Reading the file
            textBlb = TextBlob(text)            # Making our first textblob
            textCorrected = textBlb.correct()   # Correcting the text
        Correcttxt.insert(END,textCorrected)    
        Correcttxt.pack()
    
    
def handle_click(event):
    print("The spell check has started!")
    print(input(""))

    button.bind("<Button-1>", handle_click)

if __name__ == "__main__":
    spellcheck()



