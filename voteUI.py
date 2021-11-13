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

for user in users:
    post = UserPost(Image.open("user_post.png"), "hi")
    user.addPost(post)

for _ in range(3):
    for _ in range(3):
        users[random.randint(0, 4)].votePost(users[random.randint(0, 4)].getPost())
    users[random.randint(0, 4)].unvotePost(users[random.randint(0, 4)].getPost())

# most voted in left up corner
users.sort(key = lambda x: x.getPost().getVoteCount(), reverse = True)

root = Tk()
root.geometry("380x640")
root.resizable(0, 0)

username0 = Label(root,text=users[0].getUsername(),bg="white")
username0.config(font=("Arial",20))
username0.place(x=55,y=18)

profile0 = ImageTk.PhotoImage(Image.open("images-0.jpg").resize((20,20), Image.ANTIALIAS))
p0 = Label(root,image=profile0)
p0.place(x=20,y=20)

post0 = ImageTk.PhotoImage(Image.open("user_post_0.png").resize((165,165), Image.ANTIALIAS))
p0 = Label(root,image=post0)
p0.place(x=10,y=50)

count0 = Label(root,text=users[0].getPost().getVoteCount(),bg="white")
count0.config(font=("Arial",20))
count0.place(x=55,y=220)

username1 = Label(root,text=users[1].getUsername(),bg="white")
username1.config(font=("Arial",20))
username1.place(x=240,y=18)

profile1 = ImageTk.PhotoImage(Image.open("images-1.jpg").resize((20,20), Image.ANTIALIAS))
p1 = Label(root,image=profile1)
p1.place(x=205,y=20)

post1 = ImageTk.PhotoImage(Image.open("user_post_0.png").resize((165,165), Image.ANTIALIAS))
p1 = Label(root,image=post1)
p1.place(x=195,y=50)

count1 = Label(root,text=users[1].getPost().getVoteCount(),bg="white")
count1.config(font=("Arial",20))
count1.place(x=240,y=220)

username2 = Label(root,text=users[2].getUsername(),bg="white")
username2.config(font=("Arial",20))
username2.place(x=55,y=253)

profile2 = ImageTk.PhotoImage(Image.open("images-2.jpg").resize((20,20), Image.ANTIALIAS))
p2 = Label(root,image=profile2)
p2.place(x=20,y=255)

post2 = ImageTk.PhotoImage(Image.open("user_post_0.png").resize((165,165), Image.ANTIALIAS))
p2 = Label(root,image=post2)
p2.place(x=10,y=285)

count2 = Label(root,text=users[2].getPost().getVoteCount(),bg="white")
count2.config(font=("Arial",20))
count2.place(x=55,y=455)

username3 = Label(root,text=users[3].getUsername(),bg="white")
username3.config(font=("Arial",20))
username3.place(x=240,y=253)

profile3 = ImageTk.PhotoImage(Image.open("images-3.jpg").resize((20,20), Image.ANTIALIAS))
p3 = Label(root,image=profile3)
p3.place(x=205,y=255)

post3 = ImageTk.PhotoImage(Image.open("user_post_0.png").resize((165,165), Image.ANTIALIAS))
p3 = Label(root,image=post2)
p3.place(x=195,y=285)

count3 = Label(root,text=users[3].getPost().getVoteCount(),bg="white")
count3.config(font=("Arial",20))
count3.place(x=240,y=455)

username4 = Label(root,text=users[4].getUsername(),bg="white")
username4.config(font=("Arial",20))
username4.place(x=55,y=488)

profile4 = ImageTk.PhotoImage(Image.open("images-4.jpg").resize((20,20), Image.ANTIALIAS))
p4 = Label(root,image=profile4)
p4.place(x=20,y=490)

post4 = ImageTk.PhotoImage(Image.open("user_post_0.png").resize((165,165), Image.ANTIALIAS))
p4 = Label(root,image=post4)
p4.place(x=10,y=520)

count4 = Label(root,text=users[4].getPost().getVoteCount(),bg="white")
count4.config(font=("Arial",20))
count4.place(x=55,y=690)

tk.mainloop()
