#!/usr/bin/python3
"""Module for fetching subreddit information from Reddit API."""

import requests

def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if an error occurs.
    """
    # Set a descriptive user agent
    headers = {'User-Agent': 'Subreddit Info Fetcher'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Use a context manager to handle the HTTP session
    with requests.Session() as client:
        client.headers.update(headers)

        # Make the GET request to the Reddit API
        try:
            response = client.get(url, allow_redirects=False)

            # Check for a successful response
            if response.status_code == 200:
                # Extract and return the number of subscribers
                return response.json()["data"]["subscribers"]
            else:
                print(f"Error: {response.status_code} - Unable to fetch subreddit information.")
                return 0
        except requests.RequestException as e:
            print(f"Error: {e} - Unable to connect to the Reddit API.")
            return 0;

