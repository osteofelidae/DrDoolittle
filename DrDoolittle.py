import praw

reddit = praw.Reddit(
    client_id="oghQpvu_5ScijfsD5rbTJA",
    client_secret="b5TGrTBn_wzoqQJqOzifRoPEydYWvA",
    password="HanYang8176",
    user_agent="DrDoolittle",
    username="osteofelidae"
)

print(reddit.user.me())

subreddit = reddit.subreddit("BotsPlayHere")
print(subreddit.description)