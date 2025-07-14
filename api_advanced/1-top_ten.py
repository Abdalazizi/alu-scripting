#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first
10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the top 10 hot posts for a given subreddit.
    If the subreddit is invalid or unavailable, prints None.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "python:alx.api.advanced:v1.0 (by /u/alx_student)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code != 200:
            print("None")
            return

        data = response.json().get("data", {})
        posts = data.get("children", [])

        for post in posts[:10]:
            print(post.get("data", {}).get("title"))
    except Exception:
        print("None")
