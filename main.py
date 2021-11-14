import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
import UI
import gacha
import randomitem
import voteUI

def cancel():
	root.destroy()
def healthy():
	cancel()
	UI.run()
def gaacha():
	cancel()
	gacha.gachaa()
def randi():
	cancel()
	randomitem.random_item()
def community():
	cancel()
	voteUI.vote()
	
root=Tk()
root.title("Portal")
root.geometry("800x460")
root.resizable(0,0)

l1=Label(root, text="Healthy Lifestyle")
l1.grid(row=0, column=0)

l1=Label(root, text="Gacha")
l1.grid(row=0, column=1)

l1=Label(root, text="Random Box")
l1.grid(row=0, column=2)

l1=Label(root, text="Community")
l1.grid(row=0, column=3)

b1=Button(root, text="Go", width=12, command=healthy)
b1.grid(row=1, column=0)

b1=Button(root, text="Go", width=12, command=gaacha)
b1.grid(row=1, column=1)

b1=Button(root, text="Go", width=12, command=randi)
b1.grid(row=1, column=2)

b1=Button(root, text="Go", width=12, command=community)
b1.grid(row=1, column=3)

b1=Button(root, text="Close Window", width=12, command=cancel)
b1.grid(sticky="E", row=2, column=3)

col_count, row_count = root.grid_size()

for col in range(col_count):
	root.grid_columnconfigure(col, minsize=190)

for row in range(row_count):
	root.grid_rowconfigure(row, minsize=50)
root.mainloop()
