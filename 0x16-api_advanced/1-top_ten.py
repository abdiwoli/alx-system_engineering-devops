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
