#!/usr/bin/python3
""" module """
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers to the subreddit.
    If the subreddit is not found or an error occurs, returns 0.
    """
    try:
        url = f"https://www.reddit.com/r/{subreddit}/about.json"
        headers = {'User-Agent': 'CustomUserAgent/1.0'}
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            subreddit_info = response.json()
            subscribers_count = subreddit_info.get('data', {}).get('subscribers', 0)
            return subscribers_count
        else:
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"Error: {e}")
    return 0
