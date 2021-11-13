from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image
import random
import os
root = Tk()
root.geometry("380x640")
root.resizable(0, 0)
sa = ttk.Separator(root, orient='horizontal')
sb = ttk.Separator(root, orient='horizontal')
round =  ImageTk.PhotoImage(Image.open("rounded_widget.png").resize((320,80), Image.ANTIALIAS))
roundy = Label(root,image=round)
roundy.place(x=20,y=280)
img = ImageTk.PhotoImage(Image.open("walking_cathay.png").resize((320,220), Image.ANTIALIAS))
panel = Label(root, image = img)
panel.place(x=20,y=0)
sa.place(x=0,y=290)
asian = ImageTk.PhotoImage(Image.open("asiamiles.png").resize((28,28), Image.ANTIALIAS))
a = Label(root,image=asian,bg="white")
a.place(x= 50, y=300)
asianmiles = Label(root,text="7,642",bg="white")
asianmiles.config(font=("Arial", 30))
asianmiles.place(x=100,y=293)
asianadd = Label(root,text="+3",bg="white")
asianadd.config(font=("Arial",30))
asianadd.place(x=280,y=293)
c = 0
def walk(label):
    c = 0
    def count():
        global c
        c +=1
        label.config(text=str(c))
        label.after(random.randint(100,700),count)
    count()
rc = tk.Label(root,fg="black",font=("Arial",12))
rc.place(x=100,y=505)
walk(rc)

tk.mainloop()
