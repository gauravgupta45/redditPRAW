import praw

reddit = praw.Reddit(
		user_agent="script by r/user-name",
                client_id='id',
                client_secret='secret',
                username='user-name'
                password='userpassword'
		)

file1 = open('./subRedditList.txt', 'r')

Lines = file1.readlines()
for line in Lines:
	print("Line: {}".format(line.strip()))
	reddit.subreddit(line.strip()).subscribe()
