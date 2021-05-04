from tkinter import *
import tkinter as tk
from tkinter import ttk
from functools import partial
import pandas as pd
import csv 
import sys
import re
from synonym_exUI import *
from MC import *
from spellcheck_exUI import *
from worddefine import *
#data
df = pd.read_csv('user.csv')

#frame
loginWindow = Tk() 



def login():
    loginWindow.geometry('400x150')  
    loginWindow.title('The Application: An English Word Learner')

#username label and text entry box
    usernameLabel = Label(loginWindow, text="User Name").grid(row=0, column=0)
    username = StringVar()
    
    usernameEntry = Entry(loginWindow, textvariable=username).grid(row=0, column=1)   
    loginButton = Button(loginWindow, text="Login", command=lambda: Checkname(username.get()) ).grid(row=4, column=0)
    loginWindow.mainloop()
    
def Checkname(name):
    if name in df.values:
        userdata = df[df['user'] == name]
        Menu(userdata)
        loginWindow.destroy()
    else:
        print("F")
        newuser = [name,0]
        with open('user.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(newuser)
        f.close()
        Menu(newuser)


    
    

def rank():
    rankWindow = Tk()
    tree = ttk.Treeview(rankWindow)
    sorteddf = df.sort_values(by =['score'])
    #print(sorteddf)
    
    df_col = df.columns[:]
    tree["columns"]=(df_col)
    counter = len(sorteddf)
    rowLabels = sorteddf.index.tolist()
#generating for loop to create columns and give heading to them through df_col var.
    for x in range(len(df_col)):
        tree.column(x, width=100 )
        tree.heading(x, text=df_col[x])
#generating for loop to print values of dataframe in treeview column.
    for i in range(counter): 
        tree.insert('', 0, text=rowLabels[i], values=sorteddf.iloc[i].tolist())
    
    tree.column("#0", width = 0)
    tree.pack()

def dictionary():
    dictWindow = Tk();
    dictWindow.geometry('400x150')  
    dictWindow.title('Dictionary')

#username label and text entry box
    targetLabel = Label(dictWindow, text="Target").grid(row=4, column=0)
    targetVar= StringVar()
    
    targetEntry = Entry(dictWindow, textvariable=targetVar).grid(row=2, column=0)   
    searchButton = Button(dictWindow, text="Serach", command=lambda: Serach(targetVar.get()) ).grid(row=3, column=0)
    quitButton = Button(dictWindow, text="back to menu", command=lambda : dictWindow.destroy() ).grid(row=6, column=0)
    Result = Text(dictWindow)
  
    def Serach(t):
        res = []
        
        with open('dict.txt', 'r') as f: 
             for item in f: 
                 if item.startswith(t): 
                     res.append(item) 
        for x in res:
            Result.insert(END, x )
        Result.grid(row=4,column =0)

def Menu(data):
    name_var = data['user'].to_string(index=False)
    score_var = data['score'].to_string(index=False)
    menuWindow = Tk()
    menuWindow.title("Menu")
    menuWindow.geometry("400x250")
    Label1 = Label(menuWindow, text ="Main Menu").pack()
    Label2 = Label(menuWindow, text ="Name: " + name_var).pack()
    Label3 = Label(menuWindow, text ="Total Score: " + score_var).pack()
    Button1 = Button(menuWindow, text="spellcheck",command=spellcheck).pack()
    Button6 = Button(menuWindow, text="word define",command=worddefine).pack()
    Button2 = Button(menuWindow, text="MC game",command = MCgame).pack()
    Button3 = Button(menuWindow, text="Find Synonym", command =lambda :synonym(name_var,score_var)).pack()
    Button4 = Button(menuWindow, text="dictionary",command = dictionary).pack()
    Button5 = Button(menuWindow, text="ranking",command = rank).pack()
    


if __name__ == '__main__':
    login()
    

    
