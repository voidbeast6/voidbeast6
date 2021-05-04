from tkinter import *
import tkinter as tk
from tkinter import ttk
from functools import partial
import pandas as pd
import csv 
import sys
import re
from synonym_ex import *

df = pd.read_csv('user.csv')

def synonym(name,score):
    print(name)
    synonymWindow = Tk()
    rand = WordList.pickWord(WordList("dict.txt"))
    
    synonymWindow.geometry('400x150')  
    synonymWindow.title('Find Synonyms')
    nameLabel = Label(synonymWindow, text ="Welcome! " + name).grid(row=0,column=24)

    
    questionLabel = Label(synonymWindow, text="Write one Synonym of " + rand[0]).grid(row=0, column=0)
    ansgetVar= StringVar()
    
    ansgetEntry = Entry(synonymWindow, textvariable=ansgetVar).grid(row=1, column=0)   
    SubmitButton = Button(synonymWindow, text="Submit", command=lambda: Checkans(ansgetVar.get(),rand[0],int(score),name)).grid(row=3, column=0)
    quitButton = Button(synonymWindow, text="back to menu", command=lambda : synonymWindow.destroy() ).grid(row=6, column=0)
    Result = Label(synonymWindow)
    
    def Checkans(ans,rand,score,name):
        findsynonmy(rand)
        print(set(synonyms))
        if ans in synonyms:
            print("Correct")
            Result.config(text = "Answer Correct +1 point")
            update(name, score)
        else:
            print("Wrong")
            Result.config(text = "Answer Wrong, Try again")
            
        Result.grid(row=4,column =0)

    
    def update(name,score):
        
        
        df.loc[df['user'].str.lower() == name.strip(), 'score'] += 1
        print(df)
        
        df.to_csv("user.csv")
    