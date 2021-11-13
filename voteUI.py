from userClass import User # classes to get the usernames of the users
from userClass import UserPost
from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image
import string
import random
import os

# assume 5 users in the prototype, and the current user is users[0]
users = []
for i in range(5):
    username = "".join(random.choices(string.ascii_lowercase + string.digits,
                k = random.randint(6, 10))) + str(i)
    profilePic = Image.open("images-" + str(i) + ".jpg")
    descr = random.choice(["Hi", "Nice to meet you", "I'm fine thank you"])
    password = "".join(random.choices(string.ascii_lowercase
                + string.ascii_uppercase +string.digits, k = random.randint(6, 10)))

    while (username in [user.getUsername() for user in users]):
        username = "".join(random.choices(string.ascii_lowercase + string.digits,
                    k = random.randint(6, 10))) + str(i)

    users.append(User(i, username, profilePic, descr, password))

root = Tk()
root.geometry("380x640")
root.resizable(0, 0)

username0 = Label(root,text=users[0].getUsername(),bg="white")
username0.config(font=("Arial",20))
username0.place(x=55,y=18)

profile0 = ImageTk.PhotoImage(Image.open("images-0.jpg").resize((20,20), Image.ANTIALIAS))
p0 = Label(root,image=profile0)
p0.place(x=20,y=20)

post0 = ImageTk.PhotoImage(Image.open("user_post.png").resize((185,185), Image.ANTIALIAS))
p0 = Label(root,image=post0)
p0.place(x=0,y=50)

username1 = Label(root,text=users[1].getUsername(),bg="white")
username1.config(font=("Arial",20))
username1.place(x=240,y=18)

profile1 = ImageTk.PhotoImage(Image.open("images-1.jpg").resize((20,20), Image.ANTIALIAS))
p1 = Label(root,image=profile1)
p1.place(x=205,y=20)

post1 = ImageTk.PhotoImage(Image.open("user_post.png").resize((185,185), Image.ANTIALIAS))
p1 = Label(root,image=post1)
p1.place(x=185,y=50)

tk.mainloop()