import numpy as np
from datetime import datetime
from threading import Thread
from time import sleep
import sys
import random

def gacha():
	
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
