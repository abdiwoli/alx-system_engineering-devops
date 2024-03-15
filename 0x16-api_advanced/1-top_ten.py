#!/usr/bin/python3
"""" to ten """
import requests


def top_ten(subreddit):
    """Gets the titles of the first 10 hot posts in a subreddit."""
    headers = {
        'User-Agent': 'My User Agent 1.0',
    }
    try:
        res = requests.get('https://www.reddit.com/r/' + subreddit + '/hot.json?limit=10', headers=headers, allow_redirects=False)
        subreddit_data = res.json()

        if 'error' in subreddit_data:
            print('None')
        else:
            data = subreddit_data.get('data', {})
            children = data.get('children', [])
            for post in children:
                post_data = post.get('data', {})
                title = post_data.get('title')
                if title:
                    print(title)
                else:
                    print("Error: Missing 'title' field in post data")

    except Exception as e:
        print('None')
