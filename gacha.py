import numpy as np
from datetime import datetime
from threading import Thread
from time import sleep
import sys
import random
import pygame
import tkinter as tk
from PIL import ImageTk, Image

def gacha(pie_png):

	def proceed():
		window.destroy()
		gacha_spin(pie_png)

	def cancel():
		window.destroy()

	window=tk.Tk()
	window.title("e-voucher Gacha")
	window.geometry("800x1200")
	window.resizable(0,0)
	
	# Create a photoimage object of the image in the path
	image1 = Image.open(pie_png)
	test = ImageTk.PhotoImage(image1)

	label1 = tk.Label(image=test)
	label1.image = test

	# Position image
	label1.place(x=0, y=0)
	
	b1=tk.Button(window, text="Draw!", width=12, command=proceed)
	b1.grid(sticky="E", row=8, column=3)

	b1=tk.Button(window, text="Cancel", width=12, command=cancel)
	b1.grid(sticky="W", row=8, column=0)

	col_count, row_count = window.grid_size()

	for col in range(col_count):
    		window.grid_columnconfigure(col, minsize=190)

	for row in range(row_count):
    		window.grid_rowconfigure(row, minsize=50)
	window.mainloop()


def gacha_spin(pie_png):
	pygame.init()
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode([600,600])
	pikachu = pygame.image.load(pie_png)
	pikachu_rect = pikachu.get_rect(center= (300,300))
	angle = 0
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			angle += 1
			screen.fill((255,255,255))
			pikachu = pygame.transform.rotozoom(pikachu,angle,1)
			pikachu_rect = pikachu.get_rect(center = (300,300))
			screen.blit(pikachu, pikachu_rect)
			pygame.display.flip()
			clock.tick(30)
	
def random_item(x):
#x is chosen category
	randdict = {"Phone":["iPhone13", "Samsung Z Flip 3", "Nokia 3310"],
			   "Stationery":["Pen", "Eraser", "Calculator"],
			   "Watch":["G-Shock", "Rolex", "Seiko"]}
	return(random.choice(randdict[x]))
	
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
