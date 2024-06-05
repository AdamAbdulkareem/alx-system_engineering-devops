#!/usr/bin/python3
"""
0-subs.py

Description:
    Module that queries the Reddit API and returns 
    the number of subscribers for a given subreddit

Functions:
    - number_of_subscribers(subreddit): Queries the Reddit API 

Author: Adam Abdulkareem
Date: 2024-06-04
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, return 0.
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0
