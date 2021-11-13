import random
import string
from PIL import Image

# modelling a user post, containing an image, a description, a vote count and the list of voters
class UserPost:
    def __init__(self, image, descr):
        self.__image = image
        self.__descr = descr
        self.__voteCount = 0
        self.__voters = []

    def getImage(self):
        return self.__image

    def setImage(self, image):
        self.__image = image

    def getDescription(self):
        return self.__descr

    def setDescription(self, descr):
        self.__descr = descr

    def getVoteCount(self):
        return self.__voteCount

    def setVoteCount(self, voteCount):
        self.__voteCount = voteCount

    def getVoters(self):
        return self.__voters

    def addVoter(self, user):
        self.__voters += [user]

    def removeVoter(self, user):
        self.__voters.remove(user)

# modelling a user, containing the id, the username, the profile description, the password, the number of miles
# and the post (if any) the user posted
class User:
    def __init__(self, accId, username, profilePic, descr, password):
        self.__accId = accId
        self.__username = username
        self.__profilePic = profilePic
        self.__descr = descr
        self.__password = password
        self.__miles = 0
        self.__post = None

    def getUsername(self):
        return self.__username
    
    def setUsername(self, username):
        self.__username = username
    
    def getProfilePic(self):
        return self.__profilePic

    def changeProfilePic(self, profilePic):
        self.__profilePic = profilePic
    
    def getDescription(self):
        return self.__descr

    def setDescription(self, descr):
        self.__descr = descr

    def getPassword(self):
        return self.__password

    def setPassword(self, password):
        self.__password = password

    def getMiles(self):
        return self.__miles
        
    def addMiles(self, miles):
        self.__miles += miles

    def payMiles(self, miles):
        if (self.__miles - miles >= 0):
            self.__miles -= miles
        else:
            print("Not enough miles!")

    def getPost(self):
        return self.__post
    
    def addPost(self, post):
        if (self.__post == None):
            self.__post = post
        else:
            print("You can only post 1 image only!")

    def deletePost(self):
        if (self.__post != None):
            self.__post = None
        else:
            print("You do not have posts to remove!")
    
    def votePost(self, post):
        if (self not in post.getVoters()):
            post.setVoteCount(post.getVoteCount() + 1)
            post.addVoter(self)

    def unvotePost(self, post):
        if (self in post.getVoters()):
            post.setVoteCount(post.getVoteCount() - 1)
            post.removeVoter(self)

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
