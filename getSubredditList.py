import praw

reddit = praw.Reddit(
		user_agent="script by r/user-name",
                client_id='id',
                client_secret='secret',
                username='user-name'
                password='userpassword'
		)

print(reddit.user.me()) # Username will be printed if auth was successful

subscribed_subreddits = list(reddit.user.subreddits(limit=None))
print(subscribed_subreddits)

