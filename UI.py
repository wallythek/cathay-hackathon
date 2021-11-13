from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from PIL import ImageTk, Image
import random
import os
import time
from threading import Thread, Lock
import numpy as np
from datetime import datetime

def UI():

	root = Tk()
	root.geometry("380x640")
	root.resizable(0, 0)

	round =  ImageTk.PhotoImage(Image.open("rounded_widget.png").resize((320,70), Image.ANTIALIAS))
	roundy = Label(root,image=round)
	roundy.place(x=20,y=280)
	img = ImageTk.PhotoImage(Image.open("walking_cathay.png").resize((320,220), Image.ANTIALIAS))
	panel = Label(root, image = img)
	panel.place(x=20,y=50)
	navbar = ImageTk.PhotoImage(Image.open("time_bar.png").resize((320,40), Image.ANTIALIAS))
	navy = Label(root,image=navbar)
	navy.place(x=20,y=5)
	asian = ImageTk.PhotoImage(Image.open("asiamiles.png").resize((28,28), Image.ANTIALIAS))
	a = Label(root,image=asian,bg="white")
	a.place(x= 50, y=300)
	asianmiles = Label(root,text="342",bg="white")
	asianmiles.config(font=("Arial", 30))
	asianmiles.place(x=100,y=293)
	asianadd = Label(root,text="+3",bg="white")
	asianadd.config(font=("Arial",30))
	asianadd.place(x=240,y=293)
	roundi =  ImageTk.PhotoImage(Image.open("rounded_widget.png").resize((320,65), Image.ANTIALIAS))
	roundiy = Label(root,image=roundi)
	roundiy.place(x=20,y=380)
	step =  ImageTk.PhotoImage(Image.open("step.png").resize((28,28), Image.ANTIALIAS))
	stepy = Label(root,image=step,bg="white")
	stepy.place(x=50,y=400)
	tns= Label(root,bg="white",text="141k",font=("Arial",30))
	tns.place(x=90,y=390)
	global c
	c = 500
	def walk(label):
    	c = 500
    	def count():
		global c
		c +=1
		label.config(text="+"+str(c))
		label.after(random.randint(300,700),count)
	count()
	rc = tk.Label(root,fg="black",font=("Arial",30),bg="white")
	rc.place(x=240,y=390)
	walk(rc)
	rounda =  ImageTk.PhotoImage(Image.open("rounded_widget.png").resize((320,100), Image.ANTIALIAS))
	roundya = Label(root,image=rounda)
	roundya.place(x=20,y=470)
	l = ImageTk.PhotoImage(Image.open("left_arrow.png").resize((28,28), Image.ANTIALIAS))
	Lr = Label(root,image=l,bg="white")
	Lr.place(x=44,y=505)
	r = ImageTk.PhotoImage(Image.open("right_arrow.png").resize((28,28), Image.ANTIALIAS))
	rr = Label(root,image=r,bg="white")
	rr.place(x=290,y=505)
	p = ImageTk.PhotoImage(Image.open("maclehose.png").resize((140,82), Image.ANTIALIAS))
	pr = Label(root,image=p,bg="white")
	pr.place(x=109,y=480)
	tk.mainloop()

def popup():
	x = int(np.random.uniform(0,60))
	global stampnum
	stampnum = 0
	def popstamp():
		master = tk.Tk()
		master.withdraw()
		response = messagebox.showinfo('Stamp', "Click to collect stamp!")
		if(response == "ok"):
			stampnum += 1
			master = tk.Tk()
			master.withdraw()
			messagebox.showinfo('Stamp', f"You now have {stampnum} stamps!")
		
	while True:
		now = str(datetime.now().time())
		if(x == int(now[3:5])):
			popstamp()
			time.sleep(60)
			
			x = int(np.random.uniform(0,60))
			
t1 = Thread(target=UI)
t2 = Thread(target=popup)
t1.start() #Calls first function
t2.start() #Calls second function to run at same time
