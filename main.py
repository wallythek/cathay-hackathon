import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
import UI

def cancel():
    window.destroy()

window=Tk()
window.title("Portal")
window.geometry("800x460")
window.resizable(0,0)

l1=Label(window, text="Healthy Lifestyle")
l1.grid(sticky="W", row=0, column=0)

l1=Label(window, text="Gacha")
l1.grid(sticky="W", row=0, column=1)

l1=Label(window, text="Community")
l1.grid(sticky="W", row=0, column=2)

b1=Button(window, text="Go", width=12, command=UI.)
b1.grid(sticky="E", row=1, column=0)

b1=Button(window, text="Go", width=12, command=gacha)
b1.grid(sticky="E", row=1, column=1)

b1=Button(window, text="Go", width=12, command=community)
b1.grid(sticky="E", row=1, column=2)

b1=Button(window, text="Close Window", width=12, command=cancel)
b1.grid(sticky="W", row=2, column=2)

col_count, row_count = window.grid_size()

for col in range(col_count):
	window.grid_columnconfigure(col, minsize=190)

for row in range(row_count):
	window.grid_rowconfigure(row, minsize=50)
