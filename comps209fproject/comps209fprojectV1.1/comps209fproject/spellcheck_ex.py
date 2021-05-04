from textblob import TextBlob
from tkinter import *

def checkspell(file):
    with open(file, "r") as f:        # Opening the test file with the intention to read
        text = f.read()                     # Reading the file
        textBlb = TextBlob(text)            # Making our first textblob
        textCorrected = textBlb.correct()   # Correcting the text
        
    
    
if __name__ == "__main__":
    root = Tk()
    root.title('SpellChecker')
    root.geometry('500x200')

    head = Label(root, text='SpellChecker,',font=('Times new roman', 14 , 'bold'))
    head.pack()
    e = Entry(root, width=200,borderwidth=5)
    e.pack()
    b = Button(root, text = 'Check', font=('Times new roman', 14 , 'bold'), fg = 'white' , bg ='black')
    b.pack()
