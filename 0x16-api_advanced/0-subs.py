#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""

import requests


def number_of_subscribers(subreddit):
    """returns the total number of subscribers for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    res = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)'}).json()
    subs = res.get("data", {}).get("subscribers", 0)
    return subs
