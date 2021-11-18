import os
from userClass import User # classes to get the usernames of the users
from userClass import UserPost
from tkinter import *
from tkinter import ttk
import tkinter as tk
import random
import string
from PIL import ImageTk, Image
import UI
import gacha
import randomitem
import voteUI

users = [User(0, "me", Image.open("images-0.jpg"), "Me", "69420nice")]
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

def login_(users):
    def takeInput(users, login):
        username = usernameInput.get("1.0", "end-1c")
        password = passwordInput.get("1.0", "end-1c")
        usernames = [user.getUsername() for user in users]
        if (username in usernames and password == users[usernames.index(username)].getPassword()):
            login.destroy()
            main(users)
            login_(users)
        else:
            wrong = Label(text="Wrong username or password!", bg="#c6e5dc", fg="red")
            wrong.place(x=75, y=520)
            
        
    login=Tk()
    login.title("Please login")
    login.geometry("380x640")
    login.resizable(0,0)
    login.config(bg="#c6e5dc")

    username = Label(text="Username", bg="#c6e5dc")
    username.place(x=100, y=330)
    usernameInput = Text(login, height=1, width=20, font="Calibri")
    usernameInput.place(x=90, y=360)

    password = Label(text="Password", bg="#c6e5dc")
    password.place(x=100, y=430)
    passwordInput = Text(login, height=1, width=20, font="Calibri")
    passwordInput.place(x=90, y=460)

    enter = Button(login, text="Enter", bg="#046464", fg="white", width=6, height=2, command=lambda:takeInput(users, login))
    enter.place(x=145, y=560)
        
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

        bg = ImageTk.PhotoImage(Image.open("login.jpg").resize((400,652), Image.ANTIALIAS))
        background = Label(root,image=bg,bg="white")
        background.place(x=-10,y=-10)
        
        b1=Button(root, text="Healthy Lifestyle", width=15, height=2, fg="white", command=healthy, bg="#046464")
        b1.grid(row=2, column=1)

        b2=Button(root, text="Gacha", width=15, height=2, command=gaacha,fg="white", bg="#046464")
        b2.grid(row=3, column=1)

        b3=Button(root, text="Random Box", width=15, height=2, command=randi,fg="white", bg="#046464")
        b3.grid(row=4, column=1)

        b4=Button(root, text="Community", width=15, height=2, command=community,fg="white", bg="#046464")
        b4.grid(row=5, column=1)

        b5=Button(root, text="Log out", width=10,fg="white", command=cancel)
        b5.grid(sticky="E", row=6, column=2)

        col_count, row_count = root.grid_size()

        for col in range(col_count):
                root.grid_columnconfigure(col, minsize=115)

        for row in range(row_count):
                root.grid_rowconfigure(row, minsize=90)
        root.mainloop()

    login.mainloop()

login_(users)
