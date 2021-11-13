from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image
import os

root = Tk()
root.geometry("800x800")

img = ImageTk.PhotoImage(Image.open("walking.png"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Hello")
slogan.pack(side=tk.LEFT)

root.mainloop()