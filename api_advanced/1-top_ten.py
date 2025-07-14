#!/usr/bin/python3
"""
Queries Reddit API and prints titles of the first 10 hot posts.
If the subreddit is invalid or errors, prints None.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a subreddit.
    If invalid subreddit or an error occurs, prints None.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "python:top_ten:v1.0 (by /u/yourusername)"}

    try:
        res = requests.get(url, headers=headers, allow_redirects=False)
        if res.status_code != 200:
            print(None)
            return

        data = res.json().get("data", {})
        posts = data.get("children", [])
        if not posts:
            print(None)
            return

        for post in posts[:10]:
            print(post.get("data", {}).get("title"))

    except Exception:
        print(None)
