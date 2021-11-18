import os
from userClass import User # classes to get the usernames of the users
from userClass import UserPost
import tkinter as tk
from tkinter import *
from tkinter import ttk
import random
import string
from PIL import ImageTk, Image
import UI
import gacha
import randomitem
import voteUI

users = [User(0, "me", Image.open("images-0.jpg"), "Me", "69420")]
for i in range(1, 6):
    username = "".join(random.choices(string.ascii_lowercase + string.digits,
            k = random.randint(6, 10)))
    profilePic = Image.open("images-" + str(i) + ".jpg")
    descr = random.choice(["Hi", "Nice to meet you", "I'm fine thank you"])
    password = "".join(random.choices(string.ascii_lowercase
            + string.ascii_uppercase +string.digits, k = random.randint(6, 10)))

    while (username in [user.getUsername() for user in users]):
        username = "".join(random.choices(string.ascii_lowercase + string.digits,
            k = random.randint(6, 10)))

    users.append(User(i, username, profilePic, descr, password))

for i, user in enumerate(users):
    post = UserPost(Image.open("user_post_"+str(i)+".png"), "hi")
    user.addPost(post)

for _ in range(3):
    for _ in range(3):
        users[random.randint(0, 4)].votePost(users[random.randint(0, 4)].getPost())
        users[random.randint(0, 4)].unvotePost(users[random.randint(0, 4)].getPost())

def main(users):
    def cancel():
            root.destroy()
    def healthy():
            cancel()
            UI.run(users)
            main(users)
    def gaacha():
            cancel()
            gacha.gachaa()
            main(users)
    def randi():
            cancel()
            randomitem.random_item()
            main(users)
    def community(users_ = users):
            cancel()
            voteUI.vote(users_)
            users_.sort(key = lambda x: x.getPost().getVoteCount(), reverse = True)
            main(users)
            
    root=Tk()
    root.title("Portal")
    root.geometry("380x640")
    root.configure(bg="#c6e5dc")

    
    
    b1=Button(root, text="Healthy Lifestyle", width=15, height=2, command=healthy, bg="#046464", fg="white")
    b1.grid(row=2, column=1)

    b1=Button(root, text="Gacha", width=15, height=2, command=gaacha, bg="#046464", fg="white")
    b1.grid(row=3, column=1)

    b1=Button(root, text="Random Box", width=15, height=2, command=randi, bg="#046464", fg="white")
    b1.grid(row=4, column=1)

    b1=Button(root, text="Community", width=15, height=2, command=community, bg="#046464", fg="white")
    b1.grid(row=5, column=1)

    b1=Button(root, text="Close Window", width=10, command=cancel, bg="#046464", fg="white")
    b1.grid(sticky="E", row=6, column=2)

    col_count, row_count = root.grid_size()

    for col in range(col_count):
            root.grid_columnconfigure(col, minsize=115)

    for row in range(row_count):
            root.grid_rowconfigure(row, minsize=90)
    root.mainloop()

main(users)
