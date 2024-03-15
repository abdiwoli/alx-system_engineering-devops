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

        if 'data' in subreddit_data and 'children' in subreddit_data['data']:
            for post in subreddit_data['data']['children']:
                if 'data' in post and 'title' in post['data']:
                    print(post['data']['title'])
                else:
                    print("Error: Missing 'title' field in post data")
        else:
            print("Error: Unexpected data structure in subreddit response")

    except Exception as e:
        print('None')
