KEYWORD = "dog"
RESPONSE = "WOOF"

import time
import praw

reddit = praw.Reddit(
    client_id="5sZupUPFN4GLN72MIxDhGg",
    client_secret="	jLtqBp3Xh_NFKj_B0pBhjYav_5n3cg",
    password=input("Input password... "),
    user_agent="WoofBot",
    username="FindingDog"
)
time.sleep(1)
print("Logged in as " + reddit.user.me())

subreddit = reddit.subreddit(input("Enter subreddit... "))
print("Connected to r/" + subreddit.display_name)

postlist = subreddit.new()
for submission in postlist:
    postcontents = submission.selftext
    posttitle = submission.title
    
    if ("dog" in postcontents.lower()) or ("dog" in posttitle.lower()):
        
        print("Found keyword " + KEYWORD + " in post titled: " + submission.title)
        
        commentidlist = submission.comments.list()
        commented = False
        for comment in commentidlist:
            if comment.author == "FindingDog":
                commented = True
        if commented == False:
            submission.reply(RESPONSE)
