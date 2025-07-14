#!/usr/bin/python3
"""
This module queries the Reddit API to get the number of subscribers
for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid or causes an error, returns 0.
    """
    if not isinstance(subreddit, str) or subreddit == "":
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': 'python:holberton.subscriber:v1.0 (by /u/fake_user_123)'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0
        return response.json().get("data", {}).get("subscribers", 0)
    except Exception:
        return 0

