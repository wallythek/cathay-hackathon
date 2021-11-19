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
import sys
import random
import pygame
import tkinter as tk
from PIL import ImageTk, Image
import time
from tkinter import messagebox
from tkinter.ttk import *


def gachaa():
    pie_png = "newpikachu.png"
    def proceed():
        window.destroy()
        gacha_spin(pie_png)

    def cancel():
        window.destroy()

    window=tk.Tk()
    window.title("e-voucher Gacha")
    window.geometry("380x640+0+0")
    window.resizable(0,0)
	
    # Create a photoimage object of the image in the path
    image1 = Image.open("pikachu.png")
    test = ImageTk.PhotoImage(image1)

    label1 = tk.Label(image=test)
    label1.image = test

    # Position image
    label1.place(x=-100, y=80)
	
    b1=tk.Button(window, text="Draw!", width=12, command=proceed)
    b1.grid(row=10, column=1)

    b1=tk.Button(window, text="Cancel", width=12, command=cancel)
    b1.grid(row=10, column=0)

    col_count, row_count = window.grid_size()

    for col in range(col_count):
        window.grid_columnconfigure(col, minsize=190)

    for row in range(row_count):
        window.grid_rowconfigure(row, minsize=50)
    window.mainloop()


def gacha_spin(pie_png):
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode([380,640])
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
        print(angle)
        screen.fill((255,255,255))
        pikachu = pygame.transform.rotozoom(pikachu,angle,1)
        pikachu_rect = pikachu.get_rect(center = (190,320))
        screen.blit(pikachu, pikachu_rect)
        screen.blit(finger, finger_rect)
        pygame.display.flip()
        x+=1
        print(x)
        time.sleep(0.1)
        
    if (x>=12 and x<=14):
        prize="Apple Store $100 e-voucher"
    elif (x>=15 and x<=18):
        prize="Adidas $200 e-voucher"
    elif (x<=11 and x>=9):
        prize="ParknShop $50 e-voucher"
    elif(x == 5 or x == 10):
        prize="Kowloon Shangri-La 1-night-staycation voucher"
    else:
        prize="an error"
        print(x)
    master = tk.Tk()
    master.withdraw()
    messagebox.showinfo('Prize', f"You got {prize}!")
    while True:
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            Font=pygame.font.SysFont('arial', 12)
#back to home screen
            if event.type == pygame.QUIT:
                break
			#checks if a mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
            #if the mouse is clicked on the
            # button the game is terminated
                if (mouse[0]>=50 and mouse[0] <= 126) and (mouse[1]>=560 and mouse[1] <= 600):
                    break
                elif (mouse[0]>=254 and mouse[0] <= 330) and (mouse[1]>=560 and mouse[1] <= 600):
                    gacha_spin(pie_png)
#back button color
            if (mouse[0]>=50 and mouse[0] <= 126) and (mouse[1]>=560 and mouse[1] <= 600):
                pygame.draw.rect(screen,(56,126,121),(50,560,76,40))
                home=Font.render("Home", False, (255,255,255), None)
                newgame=Font.render("Again", False, (255,255,255), None)
                screen.blit(home, (75, 570))
                screen.blit(newgame, (278, 570))
            elif(mouse[0]>=254 and mouse[0] <= 330) and (mouse[1]>=560 and mouse[1] <= 600):
                pygame.draw.rect(screen,(56,126,121),(254,560,76,40))
                home=Font.render("Home", False, (255,255,255), None)
                newgame=Font.render("Again", False, (255,255,255), None)
                screen.blit(home, (75, 570))
                screen.blit(newgame, (278, 570))
            else:
                pygame.draw.rect(screen,(0,93,99),(50,560,76,40))
                pygame.draw.rect(screen,(0,93,99),(254,560,76,40))
                home=Font.render("Home", False, (255,255,255), None)
                newgame=Font.render("Again", False, (255,255,255), None)
                screen.blit(home, (75, 570))
                screen.blit(newgame, (278, 570))
            pygame.display.flip()
            
    pygame.quit()
    sys.exit()
