#!/usr/bin/python3
"""
Fetches and prints the titles of the first 10 hot posts
for a given subreddit using the Reddit API.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the top 10 hot posts for a given subreddit.
    If the subreddit is invalid or causes an error, do nothing.
    """
    if not isinstance(subreddit, str) or subreddit == "":
        return

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "python:top-ten.hot.posts:v1.0 (by /u/fake_user_123)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return

        posts = response.json().get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))

    except Exception:
        return

