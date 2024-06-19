#!/usr/bin/python3
""" queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    url = "https://api.reddit.com/r/{}?sort=hot&limit=10".format(subreddit)
    headers = {
        "User-Agent": "Python/requests:subreddit.hot.post.fetcher:v1.0 (by /u/ZainAlabidin)"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts:
            print(post["data"]["title"])
    else:
        print(None)
