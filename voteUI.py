from userClass import User # classes to get the usernames of the users
from userClass import UserPost
from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image
import string
import random
import os

# assume 6 users in the prototype, and the current user is users[0]
def vote(users):
# most voted in left up corner
    gx = 10  #offset of alignment
    users.sort(key = lambda x: x.getPost().getVoteCount(), reverse = True)
    own = 0
    for i, user in enumerate(users):
        if (user.getAccId() == 0):
            own = i
            break
    root = Tk()
    root.title("Community")
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
    likeButtons = []
    dislikeButtons = []
    tempimage = ImageTk.PhotoImage(Image.open("rounded_widget.png").resize((173,220), Image.ANTIALIAS))
    globallike = ImageTk.PhotoImage(Image.open("like.png").resize((20,20), Image.ANTIALIAS))
    globaldislike = ImageTk.PhotoImage(Image.open("dislike.png").resize((20,20), Image.ANTIALIAS))
    gshare= ImageTk.PhotoImage(Image.open("share.png").resize((20,20), Image.ANTIALIAS))
    comment = ImageTk.PhotoImage(Image.open("comment.png").resize((20,20), Image.ANTIALIAS))

    homeButton = Button(root, text="Return to Home Page", command=root.destroy)
    homeButton.place(x=200,y=10)
    
    for i in range(len(users) // 2):
        for j in range(2):
         
            roundies.append(Label(root,image=tempimage))
            roundies[-1].place(x=20+185*j-gx, y=40+235*i)

            likey.append(Label(root,image=globallike,bg="#c6e5dc"))
            likey[-1].place(x=55+185*j-25,y=240+235*i+1)
            
            dislikey.append(Label(root,image=globaldislike,bg="#c6e5dc"))
            dislikey[-1].place(x=55+185*j+17,y=240+235*i+1)
            
            sharelist.append(Label(root,image=gshare,bg="#c6e5dc"))
            sharelist[-1].place(x=55+185*j+100,y=240+235*i+1)
            
            clist.append(Label(root,image=comment,bg="#c6e5dc"))
            clist[-1].place(x=55+185*j+65,y=240+235*i+1)



            usernameLabels.append(Label(root, text=users[2*i+j].getUsername(), bg="#c6e5dc"))
            usernameLabels[-1].config(font=("Calibri", 15))
            usernameLabels[-1].place(x=55+185*j, y=42+235*i)

            profileImages.append(ImageTk.PhotoImage(users[2*i+j].getProfilePic().resize((20,20), Image.ANTIALIAS)))
            profileLabels.append(Label(root,image=profileImages[-1],bg="#c6e5dc"))
            profileLabels[-1].place(x=20+185*j, y=40+235*i)

            postImages.append(ImageTk.PhotoImage(users[2*i+j].getPost().getImage().resize((165,165), Image.ANTIALIAS)))
            postLabels.append(Label(root, image=postImages[-1]))
            postLabels[-1].place(x=10+185*j, y=70+235*i)

            countLabels.append(Label(root,text=users[2*i+j].getPost().getVoteCount(),bg="#c6e5dc"))
            countLabels[-1].config(font=("Calibri",12))
            countLabels[-1].place(x=55+185*j,y=240+235*i+1)
    
    # back up line if there are odd number of users
    if (len(users) % 2 != 0):
        i = len(users) // 2
    
        roundies.append(Label(root,image=tempimage))
        roundies[-1].place(x=20-gx, y=40+235*i)
        likey.append(Label(root,image=globallike))
        likey[-1].place(x=30,y=240+235*i+1)
        dislikey.append(Label(root,image=globaldislike,bg="#c6e5dc"))
        dislikey[-1].place(x=72,y=240+235*i+1)
        sharelist.append(Label(root,image=gshare,bg="#c6e5dc"))
        sharelist[-1].place(x=155,y=240+235*i+1)
        clist.append(Label(root,image=comment,bg="#c6e5dc"))
        clist[-1].place(x=120,y=240+235*i+1)

        usernameLabels.append(Label(root, text=users[-1].getUsername(), bg="#c6e5dc"))
        usernameLabels[-1].config(font=("Calibri", 15))
        usernameLabels[-1].place(x=55, y=42+235*i)

        profileImages.append(ImageTk.PhotoImage(users[-1].getProfilePic().resize((20,20), Image.ANTIALIAS)))
        profileLabels.append(Label(root,image=profileImages[-1]))
        profileLabels[-1].place(x=20, y=40+235*i)

        postImages.append(ImageTk.PhotoImage(users[-1].getPost().getImage().resize((165,165), Image.ANTIALIAS)))
        postLabels.append(Label(root, image=postImages[-1]))
        postLabels[-1].place(x=10, y=70+235*i)

        countLabels.append(Label(root,text=users[-1].getPost().getVoteCount(),bg="#c6e5dc"))
        countLabels[-1].config(font=("Calibri",12))
        countLabels[-1].place(x=55,y=240+235*i+1)

        likeButtons.append(Button(root, image=globallike,
                            command=lambda:[users[own].votePost(users[-1].getPost()),
                            countLabels[-1].config(text=users[-1].getPost().getVoteCount())]))
        likeButtons[-1].place(x=55-25,y=240+235*i+1)

        dislikeButtons.append(Button(root, image=globaldislike,
                            command=lambda:[users[own].unvotePost(users[-1].getPost()),
                            countLabels[-1].config(text=users[-1].getPost().getVoteCount())]))
        dislikeButtons[-1].place(x=55+17,y=240+235*i+1)

    likeButtons.append(Button(root, image=globallike,
                        command=lambda:[users[own].votePost(users[0].getPost()),
                        countLabels[0].config(text=users[0].getPost().getVoteCount())]))
    likeButtons[-1].place(x=55-25,y=240+1)
    likeButtons.append(Button(root, image=globallike,
                        command=lambda:[users[own].votePost(users[1].getPost()),
                        countLabels[1].config(text=users[1].getPost().getVoteCount())]))
    likeButtons[-1].place(x=55+185-25,y=240+1)
    likeButtons.append(Button(root, image=globallike,
                        command=lambda:[users[own].votePost(users[2].getPost()),
                        countLabels[2].config(text=users[2].getPost().getVoteCount())]))
    likeButtons[-1].place(x=55-25,y=240+235+1)
    likeButtons.append(Button(root, image=globallike,
                        command=lambda:[users[own].votePost(users[3].getPost()),
                        countLabels[3].config(text=users[3].getPost().getVoteCount())]))
    likeButtons[-1].place(x=55+185-25,y=240+235+1)
    likeButtons.append(Button(root, image=globallike,
                        command=lambda:[users[own].votePost(users[4].getPost()),
                        countLabels[4].config(text=users[4].getPost().getVoteCount())]))
    likeButtons[-1].place(x=55-25,y=240+235*2+1)
    likeButtons.append(Button(root, image=globallike,
                        command=lambda:[users[own].votePost(users[5].getPost()),
                        countLabels[5].config(text=users[5].getPost().getVoteCount())]))
    likeButtons[-1].place(x=55+185-25,y=240+235*2+1)

    dislikeButtons.append(Button(root, image=globaldislike,
                        command=lambda:[users[own].unvotePost(users[0].getPost()),
                        countLabels[0].config(text=users[0].getPost().getVoteCount())]))
    dislikeButtons[-1].place(x=55+17,y=240+1)
    dislikeButtons.append(Button(root, image=globaldislike,
                        command=lambda:[users[own].unvotePost(users[1].getPost()),
                        countLabels[1].config(text=users[1].getPost().getVoteCount())]))
    dislikeButtons[-1].place(x=55+185+17,y=240+1)
    dislikeButtons.append(Button(root, image=globaldislike,
                        command=lambda:[users[own].unvotePost(users[2].getPost()),
                        countLabels[2].config(text=users[2].getPost().getVoteCount())]))
    dislikeButtons[-1].place(x=55+17,y=240+235+1)
    dislikeButtons.append(Button(root, image=globaldislike,
                        command=lambda:[users[own].unvotePost(users[3].getPost()),
                        countLabels[3].config(text=users[3].getPost().getVoteCount())]))
    dislikeButtons[-1].place(x=55+185+17,y=240+235+1)
    dislikeButtons.append(Button(root, image=globaldislike,
                        command=lambda:[users[own].unvotePost(users[4].getPost()),
                        countLabels[4].config(text=users[4].getPost().getVoteCount())]))
    dislikeButtons[-1].place(x=55+17,y=240+235*2+1)
    dislikeButtons.append(Button(root, image=globaldislike,
                        command=lambda:[users[own].unvotePost(users[5].getPost()),
                        countLabels[5].config(text=users[5].getPost().getVoteCount())]))
    dislikeButtons[-1].place(x=55+185+17,y=240+235*2+1)
    
    tk.mainloop()
