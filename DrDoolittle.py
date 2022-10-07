KEYWORD = "dog"
RESPONSE = "WOOF"


import praw

reddit = praw.Reddit(
    client_id="oghQpvu_5ScijfsD5rbTJA",
    client_secret="b5TGrTBn_wzoqQJqOzifRoPEydYWvA",
    password=input("Input password... "),
    user_agent="DrDoolittle",
    username="osteofelidae"
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
        
        if ("dog" in postcontents.lower()) or ("dog" in posttitle.lower()):
            
            print("Found keyword " + KEYWORD + " in post titled: " + submission.title)
            
            commentidlist = submission.comments.list()
            commented = False
            for comment in commentidlist:
                if comment.author == "osteofelidae":
                    commented = True
            if commented == False:
                submission.reply(RESPONSE)
except:
    print("Access error.")