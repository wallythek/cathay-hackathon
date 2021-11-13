from userClass import User # classes to get the usernames of the users
from userClass import UserPost
from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image
import random
import os

# assume 5 users in the prototype, and the current user is users[0]
users = []
for i in range(5):
    username = "".join(random.choices(string.ascii_lowercase + string.digits,
                k = random.randint(6, 10))) + str(i)
    profilePic = random.choice([Image.open("images.jpg"), Image.open("images-1.jpg"),
                Image.open("images-2.jpg"), Image.open("images-3.jpg"), Image.open("images-4.jpg")])
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
tk.mainloop()
