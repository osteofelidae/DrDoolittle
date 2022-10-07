KEYWORD = "dog"
RESPONSE = "WOOF"

configfile = open("settings.config")
configlist = configfile.readlines()
configfile.close()

print(configlist)

CLIENTID = configlist[0][:len(configlist[0])-1]
CLIENTSECRET = configlist[1][:len(configlist[1])-1]
USERAGENT = configlist[2][:len(configlist[2])-1]
USERNAME = configlist[3]

import praw

reddit = praw.Reddit(
    client_id=CLIENTID,
    client_secret=CLIENTSECRET,
    password=input("Input password... "),
    user_agent=USERAGENT,
    username=USERNAME
)

try:
    print("Logged in as " + reddit.user.me())
except:
    print("Authentication error.")

try:
    subreddit = reddit.subreddit(input("Enter subreddit... "))
    print("Connected to r/" + subreddit.display_name)
except:
    print("Subreddit connection error.")

try:
    postlist = subreddit.new()
    for submission in postlist:
        postcontents = submission.selftext
        posttitle = submission.title
        
        if (KEYWORD in postcontents.lower()) or (KEYWORD in posttitle.lower()):
            
            print("Found keyword " + KEYWORD + " in post titled: " + submission.title)
            
            commentidlist = submission.comments.list()
            commented = False
            for comment in commentidlist:
                if comment.author == USERNAME:
                    commented = True
            if commented == False:
                submission.reply(RESPONSE)
except:
    print("Access error.")