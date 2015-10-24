import praw
import dataset
import re
import time
from random import randint

REDDIT_USERNAME = '' # Bot's username
REDDIT_PASS = '' # Bot's password
MIN_WAIT = 60 # This is the least amount of time between bot replies. A minute, currently.
MAX_WAIT = 1800 # This is the most amount of time between bot replies. 30 minutes, currently.

SUBREDDIT_NAME = '' # Subreddit the bot is operating on 

def main():
    print "Logging in..."
    r = praw.Reddit(user_agent = 'Jontron Shitposter v0.1')
    r.login(REDDIT_USERNAME, REDDIT_PASS, disable_warning = True)
	print "Logged in."

    while True:
		subreddit = r.get_subreddit(SUBREDDIT_NAME)
		comments = subreddit.get_comments(limit=1)

        for comment in comments:
            if comment.id not in already_done:
				comment.reply()
				print: "Replying..."

        # Sleep time is how I'm determining what comment it replies to. There is probably a much better way to do this.
		sleepTime = randint(MIN_WAIT,MAX_WAIT)
        time.sleep(sleepTime) # Sleep time is in seconds.

if __name__ == "__main__":
    main()
