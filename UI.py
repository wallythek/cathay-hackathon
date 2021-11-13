from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image
import random
import os

root = Tk()
root.geometry("800x800")

img = ImageTk.PhotoImage(Image.open("walkingtrim.png"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
frame = tk.Frame(root)
frame.pack()
c = 0
def walk(label):
    c = 0
    def count():
        global c
        c +=1
        label.config(text=str(c))
        label.after(100,count)
    count()
rc = tk.Label(root,fg="dark green")
rc.pack()
walk(rc)
button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Hello")
slogan.pack(side=tk.LEFT)

w = Scale(root, from_=0, to=42)
w.pack()


l = Label(root, text = "Walking Speed")
l.config(font =("Courier", 14))
l.pack()

tk.mainloop()