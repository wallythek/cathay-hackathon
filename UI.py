from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image
import random
import os
root = Tk()
root.geometry("405x640")
root.resizable(0, 0)

img = ImageTk.PhotoImage(Image.open("walkingtrim.png").resize((300,205), Image.ANTIALIAS))
panel = Label(root, image = img)
panel.place(x=150,y=0)
asian = ImageTk.PhotoImage(Image.open("asiamiles.png").resize((40,40), Image.ANTIALIAS))
a = Label(root,image=asian)
a.place(x= 50, y=300)
c = 0
def walk(label):
    c = 0
    def count():
        global c
        c +=1
        label.config(text=str(c))
        label.after(random.randint(100,700),count)
    count()
rc = tk.Label(root,fg="dark green")
rc.place(x=30,y=400)
walk(rc)

tk.mainloop()
