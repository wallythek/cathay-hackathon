import numpy as np
from datetime import datetime, timedelta
from threading import Thread
from time import sleep
import sys
import random
import pygame
import tkinter as tk
from PIL import ImageTk, Image
import time
from tkinter import messagebox
from tkinter.ttk import *

def random_item():
	
	global asiamiles
	asiamiles = 10000

	randdict = {"Phone":["iPhone13", "Samsung Z Flip 3", "Nokia 3310"], "Stationery":["Pen", "Eraser", "Calculator"], "Watch":["G-Shock", "Rolex", "Seiko"], "Experience":["3-days staycation in HK", "Round Trip to Japan", "Buffet voucher"]}
	
	def proceed():
		global asiamiles
		asiamiles -= 100
		window.destroy()
		chooserand()

	def cancel():
		window.destroy()

	def chooserand():
		def choose():
			global asiamiles
			x = e1.get()
			y = random.choice(randdict[x])
			window.destroy()
			master = tk.Tk()
			master.withdraw()
			messagebox.showinfo('Prize', f"You got {y}! You now have {asiamiles} asia miles left!")


		window=tk.Tk()
		window.title("Rand surprise")
		window.geometry("500x300")
		window.resizable(0,0)
		image1 = Image.open("randombox.jpg")
		image1 = image1.resize((300, 300), Image.ANTIALIAS) ## The (250, 250) is (height, width)

		test = ImageTk.PhotoImage(image1)

		label1 = tk.Label(image=test)
		label1.image = test

	# Position image
		label1.place(x=100, y=0)
		x = 0
		clicked=tk.StringVar()
		e1=tk.ttk.Combobox(window, width=12, textvariable=clicked)
		e1['values']=list(randdict.keys())
		e1.grid(row=5, column=1)
		e1.current(0)
		e1.bind("<<ComboboxSelected>>",x)

		b1=tk.Button(window, text="Use 100 miles", width=12, command=choose)
		b1.grid(sticky="W", row=5, column=2)

		b1=tk.Button(window, text="Cancel", width=12, command=cancel)
		b1.grid(row=5, column=0)

		col_count, row_count = window.grid_size()
		for col in range(col_count):
		    window.grid_columnconfigure(col, minsize=190)

		for row in range(row_count):
		    window.grid_rowconfigure(row, minsize=50)
    
		window.mainloop()

	window=tk.Tk()
	window.title("Random surprise")
	window.geometry("740x100")
	window.resizable(0,0)
	
	
	l1=Label(window, text=f"Asia Miles you now have:          {asiamiles}")
	l1.grid(sticky="W", row=0, column=1)
	
	l1=Label(window, text=", are you sure you want to draw?")
	l1.grid(sticky="W", row=0, column=2)
	
	b1=tk.Button(window, text="Yes!", width=12, command=proceed)
	b1.grid(sticky="W", row=1, column=3)

	b1=tk.Button(window, text="Not really", width=12, command=cancel)
	b1.grid(sticky="E", row=1, column=0)

	col_count, row_count = window.grid_size()

	for col in range(col_count):
		window.grid_columnconfigure(col, minsize=190)

	for row in range(row_count):
		window.grid_rowconfigure(row, minsize=50)
	window.mainloop()
