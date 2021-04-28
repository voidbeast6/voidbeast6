from tkinter import *
import tkinter as tk
from tkinter import ttk
from functools import partial
import pandas as pd
import csv 
import sys

df = pd.read_csv('user.csv')

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
        print(userdata)
        print("T")
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

def logout():
    frame.distory()
    loginWindow.tkraise()

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

    

def Menu(data):
    name_var = data['user'].to_string(index=False)
    score_var = data['score'].to_string(index=False)
    menuWindow = Tk()
    menuWindow.title("Menu")
    menuWindow.geometry("400x250")
    Label1 = Label(menuWindow, text ="Main Menu").pack()
    Label2 = Label(menuWindow, text ="Name: " + name_var).pack()
    Label3 = Label(menuWindow, text ="Total Score: " + score_var).pack()
    Button1 = Button(menuWindow, text="game1").pack() 
    Button2 = Button(menuWindow, text="game2").pack()
    Button3 = Button(menuWindow, text="game3").pack()
    Button4 = Button(menuWindow, text="dict").pack()
    Button5 = Button(menuWindow, text="rank",command = rank).pack()
    Button6 = Button(menuWindow, text="Logout",command = logout).pack()


if __name__ == '__main__':
    login()
    

    
