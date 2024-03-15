#!/usr/bin/python3
""" import module """
import praw

def top_ten(subreddit):
    try:
        reddit = praw.Reddit(client_id='DJJOnLCqhehVpa6370yMbA',
                             client_secret='2BmbJvW4Ia7JAfm6I9pNkCqwKhXUjQ',
                             user_agent='MyRedditApp by /u/abdiwoli')

        subreddit = reddit.subreddit(subreddit)
        hot_posts = subreddit.hot(limit=10)

        for post in hot_posts:
            print(post.title)

    except Exception as e:
        print("None")

import sys


if __name__ == '__main__':
    top_ten = __import__('1-top_ten').top_ten
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
