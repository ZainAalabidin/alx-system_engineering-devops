#!/usr/bin/python3
"""
ecursive function that queries the Reddit API and
returns a list containing the titles of all hot articles for a given
subreddit. If no results are found for the given subreddit, the
function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "Python/requests:subreddit.hot.post.fetcher:v1.0"
    }
    params = {"limit": 100}
    if after:
        params["after"] = after

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )

        if response.status_code != 200:
            return None

        data = response.json().get("data", {})
        posts = data.get("children", [])
        after = data.get("after", None)

        for post in posts:
            hot_list.append(post["data"]["title"])

        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    except requests.RequestException:
        return None
