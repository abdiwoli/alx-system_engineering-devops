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
        if 'error' in subreddit_data.keys():
            print('None')
        else:
            more = subreddit_data['data']['children']
            for detail in more:
                print(detail['data']['title'])

    except Exception as e:
        print('None')
