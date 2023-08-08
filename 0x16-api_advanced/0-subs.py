#!/usr/bin/python3
"""
0-subs
=======


Description:
-------------
This python script queries the Reddit API and returns the number of
subscribers(not active users, total subscribers) for a given subreddit

Usage:
-------
python3 0.subs <subreddit name>
e.g python3 0.subs programming
"""
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Fake Agent"}
    response = requests.get(url, headers=headers)
    outcome = response.json()
    if response.status_code != 200:
        data = 0
    else:
        data = outcome.get("data").get("subscribers")
    return data
