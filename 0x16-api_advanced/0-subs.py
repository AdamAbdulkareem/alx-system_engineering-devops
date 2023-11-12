#!/usr/bin/python3
import requests
"""
Import the requests module
"""

def number_of_subscribers(subreddit):
    """
    Fetch the number of subscribers for a given subreddit

    Args:
        subreddit (string): The name of the subreddit

    Returns:
        integer: The number of subscribers
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "Fake Agent"
            }
    response = requests.get(url, headers=headers)
    outcome = response.json()

    if response.status_code != 200:
        data = 0
    else:
        data = outcome.get('data').get('subscribers')
        return data
