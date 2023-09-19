from tkinter import *
from tkinter import ttk
import os

root = Tk()
frm = ttk.Frame(root, width=560, height=420)
frm.grid()

l = Label(root, text = "Fact of the Day")
l.config(font =("Courier", 14))

def createList(listName: str, arg: list):
    with open(r'./list/list.txt' + listName, 'w') as fp:
        for i in arg:
            fp.write(i)
        return 1

def loadList(listName: str):
    pass

def refreshLists():
    pass

root.mainloop()

