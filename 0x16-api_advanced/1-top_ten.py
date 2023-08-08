#!/usr/bin/python3
"""
1-top_ten
=======


Description:
-------------
This is a python script that queries the Reddit API and prints the
titles of the first 10 hot posts listed for a given subreddit.

Usage:
-------
python3 1-top_ten <subreddit name>
e.g python3 1-top_ten programming
"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Fake Agent"}
    response = requests.get(url, headers=headers)
    outcome = response.json()

    if response.status_code == 200:
        for sub in outcome["data"]["children"]:
            print(sub["data"]["title"])
    else:
        print("None")

