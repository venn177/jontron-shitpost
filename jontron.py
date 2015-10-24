import praw
import dataset
import re
import time
import random

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
		
		random_reply = random.choice(('Sorry, I only speak to sailors.', 'Get out of our home!', 'Actually, the crowbar snapped in two.', 'Quality post!', 'I have a theory! I think ' + person1 + ' is actually ' + person2 + '!'))
		person1 = random.choice(('JonTron', 'Egoraptor', 'Arin', 'Danny', 'Jacques', 'Starcade Man'))
		person2 = random.choice(('JonTron', 'Egoraptor', 'Arin', 'Danny', 'Jacques', 'Starcade Man', 'dead'))
		
        for comment in comments:
            if comment.id not in already_done:
				comment.reply(random_reply)
				print: "Replying..."
				already_done.add(comment.id)

        # Sleep time is how I'm determining what comment it replies to. There is probably a much better way to do this.
		sleepTime = randint(MIN_WAIT,MAX_WAIT)
		print "Sleeping for " + sleepTime + " seconds..."
        time.sleep(sleepTime) # Sleep time is in seconds.

if __name__ == "__main__":
    main()
