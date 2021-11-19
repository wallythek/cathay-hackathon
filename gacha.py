import os
import numpy as np
from datetime import datetime, timedelta
from threading import Thread
from time import sleep
import sys
import random
import numpy as np
from datetime import datetime, timedelta
from threading import Thread
from time import sleep
import pygame
import tkinter as tk
from PIL import ImageTk, Image
import time
from tkinter import messagebox
from tkinter.ttk import *


def gachaa(flag):
    pie_png = "newpikachu.png"
    def proceed(flag, window):
        flag.append(False)
        flag.remove(True)
        window.destroy()
        gacha_spin(pie_png)

    def cancel():
        window.destroy()

    window=tk.Tk()
    window.title("e-voucher Gacha")
    window.geometry("380x640+0+0") # LEFT CORNER AT (0,0)
    window.config(bg="#c6e5dc")
    window.resizable(0,0)
	
    # Create a photoimage object of the image in the path
    image1 = Image.open("pikachu.png")
    test = ImageTk.PhotoImage(image1)

    label1 = tk.Label(image=test,bg="#c6e5dc")
    label1.image = test

    # Position image
    label1.place(x=-100, y=80)
    if (True in flag):
        b1=tk.Button(window, text="Draw!", bg="#046464", fg = "white", width=12, command=lambda:proceed(flag, window))
        b1.grid(row=10, column=1)

        b1=tk.Button(window, text="Cancel", bg="#046464", fg = "white", width=12, command=cancel)
        b1.grid(row=10, column=0)
    else:
        deny=tk.Label(window, text="You have already drawn the weekly gacha!", fg="red", bg="#c6e5dc")
        deny.place(x=45,y=500)
        b1=tk.Button(window, text="Return to Home Page", width=20, height=2, bg="#046464", command=cancel)
        b1.place(x=95,y=550)

    col_count, row_count = window.grid_size()

    for col in range(col_count):
        window.grid_columnconfigure(col, minsize=190)

    for row in range(row_count):
        window.grid_rowconfigure(row, minsize=50)
    window.mainloop()


def gacha_spin(pie_png):
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0) # LEFT CORNER AT (0,0)
    pygame.init()
    pygame.display.set_caption("Spin!")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode([380,640])
    screen.fill((198,229,220))
    pygame.display.flip()
    pikachu = pygame.image.load(pie_png)
    pikachu_rect = pikachu.get_rect(center= (190,320))
    finger = pygame.image.load("finger.png")
    finger = pygame.transform.scale(finger, (300, 100))
    finger_rect = finger.get_rect(center= (-100,320))
    angle = 0
    r = int(np.random.uniform(3,7))
    x = 0
    start = int(time.time())
    end = start + r
    clock.tick(10)
    while int(time.time())<end:
        angle += 2
        screen.fill((198,229,220))
        pikachu = pygame.transform.rotozoom(pikachu,angle,1)
        pikachu_rect = pikachu.get_rect(center = (190,320))
        screen.blit(pikachu, pikachu_rect)
        screen.blit(finger, finger_rect)
        pygame.display.flip()
        x+=1
        time.sleep(0.1)
    print(x)
        
    if (x>=13 and x<=14):
        prize="Apple Store $100 e-voucher"
    elif (x>=15 and x<=18):
        prize="Adidas $200 e-voucher"
    elif (x<=12 and x>=9):
        prize="ParknShop $50 e-voucher"
    elif(x == 5 or x == 10):
        prize="Kowloon Shangri-La 1-night-staycation voucher"
    else:
        prize="an error"
        print(x)
    Font=pygame.font.SysFont('arial', 18)
    gift=Font.render(f"You got {prize}!", False, (0,255,0), None)
    screen.blit(gift, (40, 60))
    Font=pygame.font.SysFont('arial', 12)
    running = True
    while (running):
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            
            #back button color
            pygame.draw.rect(screen,(56,126,121),(110,560,150,40))
            home=Font.render("Return to Home Page", False, (255,255,255), None)
            screen.blit(home, (128, 575))
            pygame.display.flip()
	    #checks if a mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                #if the mouse is clicked on the
                # button the game is terminated
                if (mouse[0]>=110 and mouse[0] <= 260) and (mouse[1]>=560 and mouse[1] <= 600):
                    running = False
                    pygame.quit()
                    break
