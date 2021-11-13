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


def gacha(pie_png):

	def proceed():
		window.destroy()
		gacha_spin(pie_png)

	def cancel():
		window.destroy()

	window=tk.Tk()
	window.title("e-voucher Gacha")
	window.geometry("740x730")
	window.resizable(0,0)
	
	# Create a photoimage object of the image in the path
	image1 = Image.open(pie_png)
	test = ImageTk.PhotoImage(image1)

	label1 = tk.Label(image=test)
	label1.image = test

	# Position image
	label1.place(x=-50, y=0)
	
	b1=tk.Button(window, text="Draw!", width=12, command=proceed)
	b1.grid(sticky="W", row=10, column=3)

	b1=tk.Button(window, text="Cancel", width=12, command=cancel)
	b1.grid(sticky="E", row=10, column=0)

	col_count, row_count = window.grid_size()

	for col in range(col_count):
    		window.grid_columnconfigure(col, minsize=190)

	for row in range(row_count):
    		window.grid_rowconfigure(row, minsize=50)
	window.mainloop()


def gacha_spin(pie_png):
	pygame.init()
	start = int(time.time())
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode([600,600])
	pikachu = pygame.image.load(pie_png)
	pikachu_rect = pikachu.get_rect(center= (300,300))
	finger = pygame.image.load("finger.png")
	finger = pygame.transform.scale(finger, (300, 600))
	finger_rect = pikachu.get_rect(center= (850,700))
	angle = 0
	r = int(np.random.uniform(20,30))
	end = start + r
	prize = "Apple voucher"
	while int(time.time())<end:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			angle += 1
			screen.fill((255,255,255))
			pikachu = pygame.transform.rotozoom(pikachu,angle,1)
			pikachu_rect = pikachu.get_rect(center = (300,300))
			screen.blit(pikachu, pikachu_rect)
			screen.blit(finger, finger_rect)
			pygame.display.flip()
			clock.tick(1)
	master = tk.Tk()
	master.withdraw()
	messagebox.showinfo('Prize', f"You got {prize}!")
	pygame.display.quit()
	
def random_item():

	randdict = {"Phone":["iPhone13", "Samsung Z Flip 3", "Nokia 3310"], "Stationery":["Pen", "Eraser", "Calculator"], "Watch":["G-Shock", "Rolex", "Seiko"], "Experience":["3-days staycation in HK", "Round Trip to Japan", "Buffet voucher"]}
	
	    def proceed():
		window.destroy()
		chooserand()

	    def cancel():
		window.destroy()

	    def chooserand():
		def choose():
		    x = e1.get()
		    y = random.choice(randdict[x])
		    window.destroy()
		    master = tk.Tk()
		    master.withdraw()
		    messagebox.showinfo('Prize', f"You got {y}!")


		window=tk.Tk()
		window.title("Rand surprise")
		window.geometry("300x50")
		window.resizable(0,0)

		x = 0
		clicked=tk.StringVar()
		e1=tk.ttk.Combobox(window, width=12, textvariable=clicked)
		e1['values']=list(randdict.keys())
		e1.grid(sticky="E", row=0, column=2)
		e1.current(0)
		e1.bind("<<ComboboxSelected>>",x)

		b1=tk.Button(window, text="Draw", width=12, command=choose)
		b1.grid(sticky="W", row=1, column=3)

		b1=tk.Button(window, text="Cancel", width=12, command=cancel)
		b1.grid(sticky="E", row=1, column=0)

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
	
	    l1=Label(window, text="Asia Miles you now have:")
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
	
def popup():
	x = int(np.random.uniform(0,60))
	while True:
		now = str(datetime.now().time())
		if(x == int(now[3:5])):
			popstamp()
			x = int(np.random.uniform(0,60))
			
"""def timer(x):
    for i in range(x):
        sleep(60)   
    popstamp() #stops program after timer runs out, you could also have it print something or keep the user from attempting to answer any longer

def question():
    answer = input("foo?")

t1 = Thread(target=timer)
t2 = Thread(target=question)
t1.start() #Calls first function
t2.start() #Calls second function to run at same time"""
