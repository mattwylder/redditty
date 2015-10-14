import praw
import os

def main():
    r = praw.Reddit(user_agent='reddpyxx')
    submissions =r.get_subreddit('linux').get_top(limit=10)
    i = 0;
    for submission in submissions:
	print str(i)+ ' ' + submission.title
	i=i+1
    #loc = raw_input('What submission?')
    submissions.__get__(2) 
main()
