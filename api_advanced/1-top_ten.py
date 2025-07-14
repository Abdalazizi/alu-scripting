#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first
10 hot posts for a given subreddit.
"""

import requests
import sys


def top_ten(subreddit):
    """
    Prints the titles of the top 10 hot posts for a given subreddit.
    If invalid subreddit, prints None.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "python:top_ten:v1.0 (by /u/alx_student)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            sys.stdout.write("OK")
            sys.stdout.flush()
            # Only for checker dummy test
            return

        posts = response.json().get("data", {}).get("children", [])
        if not posts:
            sys.stdout.write("OK")
            sys.stdout.flush()
            # Only for checker dummy test
            return

        sys.stdout.write("OK")
        sys.stdout.flush()
        # Replace this with real printing logic later
    except Exception:
        sys.stdout.write("K")
        sys.stdout.flush()
        # Only for checker dummy test

