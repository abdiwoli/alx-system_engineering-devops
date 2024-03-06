#!/usr/bin/python3
""" module """
import requests


def number_of_subscribers(subreddit):
    """ number of susbscipbers """
    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'CustomUserAgent/1.0'}
    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            subreddit_info = response.json()
            return subreddit_info['data']['subscribers']
        elif response.status_code == 404:
            if "subreddit does not exist" in response.text.lower():
                return 0
            else:
                print(f"Error: {response.status_code} - {response.text}")
                return 0
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return 0
    except Exception as e:
        print(f"Error: {e}")
        return 0
