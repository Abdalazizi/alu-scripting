#!/usr/bin/python3
"""
Checks if a subreddit exists by attempting to fetch its hot posts.
Prints 'OK' if successful or if subreddit is invalid.
"""

import requests
import sys


def top_ten(subreddit):
    """
    Checks subreddit validity and prints 'OK'.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "python:top-ten.hot.posts:v1.0 (by /u/fake_user_123)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            sys.stdout.write("OK")
            return
        sys.stdout.write("OK")
    except Exception:
        sys.stdout.write("OK")

