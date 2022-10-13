KEYWORD = "dog"
RESPONSE = "WOOF"
count = 0
count1 = 0

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
    user = reddit.user.me()
    print("Logged in as " + user)
except:
    print("Authentication error.")




import string

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

numlist = [0]
for number in range(999999999999):
    outstr = ""
    for index in numlist:
        outstr += string.ascii_lowercase[index]
    if numlist[-1] == 25:
        numlist[-1] = 0
        carry = True
    else:
        numlist[-1] += 1
        carry = False
        
    reference = len(numlist)-2
    while carry == True:
        if reference >= 0:
            if numlist[reference] < 25:
                numlist[reference] += 1
                carry = False
            else:
                numlist[reference] = 0
                carry = True
        elif reference < 0:
            numlist.insert(0,0)
            carry = False
        reference -= 1
    try:
        subreddit = outstr
        print("trying subreddit " + subreddit)
        print("Connected to r/" + subreddit.display_name)
    except:
        print("Subreddit connection error.")
    
    try:
        postlist = subreddit.new()
        for submission in postlist:
            postcontents = submission.selftext
            posttitle = submission.title
            
            if (KEYWORD in postcontents.lower()) or (KEYWORD in posttitle.lower()):
                count += 1
                print("Found keyword " + KEYWORD + " in post titled: " + submission.title)
                
                commentidlist = submission.comments.list()
                commented = False
                for comment in commentidlist:
                    if comment.author == USERNAME:
                        commented = True
                if commented == False:
                    count1 += 1
                    submission.reply(RESPONSE)
            
    except:
        print("Access error.")
    
    try:
        postlist = subreddit.top()
        for submission in postlist:
            postcontents = submission.selftext
            posttitle = submission.title
            
            if (KEYWORD in postcontents.lower()) or (KEYWORD in posttitle.lower()):
                count += 1
                print("Found keyword " + KEYWORD + " in post titled: " + submission.title)
                
                commentidlist = submission.comments.list()
                commented = False
                for comment in commentidlist:
                    if comment.author == USERNAME:
                        commented = True
                if commented == False:
                    count1 += 1
                    submission.reply(RESPONSE)
    except:
        print("Access error.")
        
    try:
        postlist = subreddit.hot()
        for submission in postlist:
            postcontents = submission.selftext
            posttitle = submission.title
            
            if (KEYWORD in postcontents.lower()) or (KEYWORD in posttitle.lower()):
                count += 1
                print("Found keyword " + KEYWORD + " in post titled: " + submission.title)
                
                commentidlist = submission.comments.list()
                commented = False
                for comment in commentidlist:
                    if comment.author == USERNAME:
                        commented = True
                if commented == False:
                    count1 += 1
                    submission.reply(RESPONSE)
    except:
        print("Access error.")
    
    print("Complete. Found " + str(count) + " dogs, commented " + str(count1) + " times.")