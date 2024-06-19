#!/usr/bin/python3
"""
queries the Reddit API and returns the
number of subscribers (not active users, total subscribers) for
a given subreddit. If an invalid subreddit is given, the function
should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """return number of subscribers"""
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    headers = {"User-Agent": "CustomClient/1.0"}
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        data = res.json()
        return data["data"]["subscribers"]
    else:
        return 0
