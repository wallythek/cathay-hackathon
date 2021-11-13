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

    users.append(User(i, username[:random.randint(5,8)], profilePic, descr, password))
i = 0
for user in users:

    post = UserPost(Image.open("user_post_"+str(i)+".png"), "hi")
    i+=1
    user.addPost(post)

for _ in range(3):
    for _ in range(3):
        users[random.randint(0, 4)].votePost(users[random.randint(0, 4)].getPost())
    users[random.randint(0, 4)].unvotePost(users[random.randint(0, 4)].getPost())

# most voted in left up corner
gx = 10  #offset of alignment
yu = 4

users.sort(key = lambda x: x.getPost().getVoteCount(), reverse = True)

root = Tk()
root.geometry("380x640")
root.resizable(0, 0)

usernameLabels = []
profileImages = []
profileLabels = []
postImages = []
postLabels = []
countLabels = []
roundies = []
likey = []
dislikey = []
sharelist = []
clist = []
tempimage = ImageTk.PhotoImage(Image.open("rounded_widget.png").resize((173,220), Image.ANTIALIAS))
globallike = ImageTk.PhotoImage(Image.open("like.png").resize((20,20), Image.ANTIALIAS))
globaldislike = ImageTk.PhotoImage(Image.open("dislike.png").resize((20,20), Image.ANTIALIAS))
gshare= ImageTk.PhotoImage(Image.open("share.png").resize((20,20), Image.ANTIALIAS))
comment = ImageTk.PhotoImage(Image.open("comment.png").resize((20,20), Image.ANTIALIAS))
for i in range(len(users) // 2):
    for j in range(2):
         
        roundies.append(Label(root,image=tempimage))
        roundies[-1].place(x=20+185*j-gx, y=20+235*i)

        likey.append(Label(root,image=globallike,bg="white"))
        likey[-1].place(x=55+185*j-25,y=220+235*i-yu+1)
        dislikey.append(Label(root,image=globaldislike,bg="white"))
        dislikey[-1].place(x=55+185*j+17,y=220+235*i-yu+1)
        sharelist.append(Label(root,image=gshare,bg="white"))
        sharelist[-1].place(x=55+185*j+100,y=220+235*i-yu+1)
        clist.append(Label(root,image=comment,bg="white"))
        clist[-1].place(x=55+185*j+65,y=220+235*i-yu+1)



        usernameLabels.append(Label(root, text=users[2*i+j].getUsername(), bg="white"))
        usernameLabels[-1].config(font=("Arial", 15))
        usernameLabels[-1].place(x=55+185*j, y=18+235*i+yu)

        profileImages.append(ImageTk.PhotoImage(users[2*i+j].getProfilePic().resize((20,20), Image.ANTIALIAS)))
        profileLabels.append(Label(root,image=profileImages[-1],bg="white"))
        profileLabels[-1].place(x=20+185*j, y=20+235*i+yu)

        postImages.append(ImageTk.PhotoImage(users[2*i+j].getPost().getImage().resize((165,165), Image.ANTIALIAS)))
        postLabels.append(Label(root, image=postImages[-1]))
        postLabels[-1].place(x=10+185*j, y=50+235*i)

        countLabels.append(Label(root,text=users[2*i+j].getPost().getVoteCount(),bg="white"))
        countLabels[-1].config(font=("Arial",12))
        countLabels[-1].place(x=55+185*j,y=220+235*i-yu+1)

if (len(users) % 2 != 0):
    i = len(users) // 2
    
    roundies.append(Label(root,image=tempimage))
    roundies[-1].place(x=20-gx, y=20+235*i)
    likey.append(Label(root,image=globallike))
    likey[-1].place(x=30,y=220+235*i-yu+1)
    dislikey.append(Label(root,image=globaldislike,bg="white"))
    dislikey[-1].place(x=72,y=220+235*i-yu+1)
    sharelist.append(Label(root,image=gshare,bg="white"))
    sharelist[-1].place(x=155,y=220+235*i-yu+1)
    clist.append(Label(root,image=comment,bg="white"))
    clist[-1].place(x=120,y=220+235*i-yu+1)

    usernameLabels.append(Label(root, text=users[-1].getUsername(), bg="white"))
    usernameLabels[-1].config(font=("Arial", 15))
    usernameLabels[-1].place(x=55, y=18+235*i+yu)

    profileImages.append(ImageTk.PhotoImage(users[-1].getProfilePic().resize((20,20), Image.ANTIALIAS)))
    profileLabels.append(Label(root,image=profileImages[-1]))
    profileLabels[-1].place(x=20, y=20+235*i+yu)

    postImages.append(ImageTk.PhotoImage(users[-1].getPost().getImage().resize((165,165), Image.ANTIALIAS)))
    postLabels.append(Label(root, image=postImages[-1]))
    postLabels[-1].place(x=10, y=50+235*i)

    countLabels.append(Label(root,text=users[-1].getPost().getVoteCount(),bg="white"))
    countLabels[-1].config(font=("Arial",12))
    countLabels[-1].place(x=55,y=220+235*i-yu+1)


tk.mainloop()
