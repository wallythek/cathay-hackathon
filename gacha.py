import numpy as np
from datetime import datetime
from threading import Thread
from time import sleep
import sys
import random
import pygame

def gacha():
	

def gacha_spin():
	pygame.init()
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode([600,600])
	pikachu = pygame.image.load("piechart.png")
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
