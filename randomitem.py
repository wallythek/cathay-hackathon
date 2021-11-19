from userClass import User # classes to get the usernames of the users
from userClass import UserPost
import numpy as np
from datetime import datetime, timedelta
from threading import Thread
from time import sleep
import sys
import random
import pygame
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import time
from tkinter import messagebox
from tkinter.ttk import *

def random_item(users):
    own = 0
    for i, user in enumerate(users):
        if (user.getAccId() == 0):
            own = i
            break

    randdict = {"Phone":["iPhone13", "Samsung Z Flip 3", "Nokia 3310"], "Stationery":["Pen", "Eraser", "Calculator"], "Watch":["G-Shock", "Seiko", "Omega"], "Experience":["3-days staycation in HK", "Round Trip to Japan", "Buffet voucher"]}
	
    def proceed(users, window):
        deny = tk.Label(window, text="You do not have enough miles!", bg="#c6e5dc", fg="red")
        if (users[own].payMiles(100)):
            window.destroy()
            chooserand(users)
        else:
            deny = tk.Label(window, text="You do not have enough miles!", bg="#c6e5dc", fg="red")
            deny.place(x=95, y=500)

    def cancel():
        window.destroy()

    def refund(users, window):
        users[own].addMiles(100)
        window.destroy()
    
    def chooserand(users):
        def choose(users, b1, b2):
            x = e1.get()
            y = random.choice(randdict[x])
            congrats1 = tk.Label(window, text=f"You got {y}!", bg="#c6e5dc", fg="green", font=("Calibri", 16))
            congrats1.place(x=30,y=50)
            congrats2 = tk.Label(window, text=f"You now have {users[own].getMiles()} Asia Miles left!", bg="#c6e5dc", fg="green", font=("Calibri", 16))
            congrats2.place(x=30,y=90)
            b1.destroy()
            b2.destroy()
            
            b3=tk.Button(window, text="Return to Home Page", width=20, height=2, fg="black", bg="#046464", command=window.destroy)
            b3.place(x=100,y=520)
            

        window = tk.Tk()
        window.title("Random surprise")
        window.geometry("380x640")
        window.config(bg="#c6e5dc")
        window.resizable(0,0)
        image1 = Image.open("randombox.png")
        image1 = image1.resize((300, 300), Image.ANTIALIAS) ## The (300, 300) is (height, width)

        test = ImageTk.PhotoImage(image1)

        label1 = tk.Label(image=test, bg="#c6e5dc")
        label1.image = test

        # Position image
        label1.place(x=45, y=130)
        x = 0
        clicked=tk.StringVar()
        e1=tk.ttk.Combobox(window, width=12, height=2, textvariable=clicked)
        e1['values']=list(randdict.keys())
        e1.place(x=120, y=450)
        e1.current(0)
        e1.bind("<<ComboboxSelected>>",x)

        b1=tk.Button(window, text="Cancel", width=12, height=2, fg="black", bg="#046464", command=lambda:refund(users, window))
        b1.grid(sticky = "E", row=10, column=0)
        
        b2=tk.Button(window, text="Use 100 miles", width=12, height=2, fg="black", bg="#046464", command=lambda:choose(users, b1, b2))
        b2.grid(sticky = "W", row=10, column=2)

        col_count, row_count = window.grid_size()
        for col in range(col_count):
            window.grid_columnconfigure(col, minsize=126)

        for row in range(row_count):
            window.grid_rowconfigure(row, minsize=50)
    
        window.mainloop()

    window=tk.Tk()
    window.title("Random surprise")
    window.geometry("380x640")
    window.config(bg="#c6e5dc")
    window.resizable(0,0)

    bg_ = ImageTk.PhotoImage(Image.open("random.jpg").resize((711, 400), Image.ANTIALIAS))
    background_ = tk.Label(window,image=bg_,bg="#c6e5dc")
    background_.place(x=-10,y=-30)
    
    l1=tk.Label(window, text="You now have " + str(users[own].getMiles()) + " Asia Miles,", bg="#c6e5dc", font=("Calibri", 18))
    l1.place(x=30,y=400)
	
    l1=tk.Label(window, text="are you sure you want to draw?", bg="#c6e5dc", font=("Calibri", 18))
    l1.place(x=30,y=450)
	
    b1=tk.Button(window, text="Yes!", width=12, height=2, fg="black", bg="#046464", command=lambda:proceed(users, window))
    b1.grid(row=11, column=1)

    b1=tk.Button(window, text="Not really", width=12, height=2, fg="black", bg="#046464", command=cancel)
    b1.grid(row=11, column=0)

    col_count, row_count = window.grid_size()

    for col in range(col_count):
        window.grid_columnconfigure(col, minsize=190)

    for row in range(row_count):
        window.grid_rowconfigure(row, minsize=50)
    window.mainloop()
