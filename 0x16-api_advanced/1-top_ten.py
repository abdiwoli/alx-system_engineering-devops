#!/usr/bin/python3
"""hot 10 request"""
import requests


def top_ten(subreddit):
    """gets the hostest 10 from api"""
    headers = {
        'User-Agent': 'My User Agent 1.0',
    }
    try:
        res = requests.get('https://www.reddit.com/r/'+subreddit
                           + '/hot.json?limit=10', headers=headers,
                           allow_redirects=False)
        subreddit_data = res.json()
    except Exception as e:
        print('None')
    if 'error' in subreddit_data.keys():
        print('None')
    else:
        more = subreddit_data['data']['children']
        for m in more:
            print(m['data']['title'])
