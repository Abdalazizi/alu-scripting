#!/usr/bin/python3
"""
This module queries the Reddit API to return the number of subscribers
for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "python:sub.count:v1.0 (by /u/fakeuser123)"
    }

    try:
        response = requests.get(
            url, headers=headers, allow_redirects=False, timeout=10)

        if response.status_code != 200:
            return 0

        data = response.json().get("data", {})
        return data.get("subscribers", 0)

    except (requests.RequestException, ValueError, KeyError):
        return 0

