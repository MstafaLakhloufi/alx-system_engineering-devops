#!/usr/bin/python3
"""
Uses Reddit API to print the number of subscribers of a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit.
    Returns 0 if the subreddit is invalid or request fails.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}
    
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    try:
        data = response.json().get("data")
        if data and "subscribers" in data:
            return data.get("subscribers", 0)
        else:
            return 0
    except (ValueError, KeyError):
        return 0
