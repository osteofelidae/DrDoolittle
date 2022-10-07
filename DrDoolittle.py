import praw
import webbrowser

reddit = praw.Reddit(
    client_id = "EiyCgfRwTXEUOVHT-4v94A",
    client_secret = "bUVz3deV6zcPEKszuGHMdvV-AcaSeA",
    redirect_uri="http://localhost:8080",
    user_agent = "DrDoolittle"
)

webbrowser.open(reddit.auth.url(scopes=["identity"], state="...", duration="permanent"))

inputurl = input ("Input url... ")
print(reddit.auth.authorize(inputurl[38:68]))

print(reddit.user.me())

subreddit = reddit.subreddit("BotsPlayHere")
print(subreddit.description)