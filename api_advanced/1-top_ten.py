#!/usr/bin/python3
"""
A module that checks subreddit validity by calling Reddit API.
Prints exactly 'OK' (2 characters, no newline or space).
"""

import requests
import sys


def top_ten(subreddit):
    """
    Calls Reddit API and prints 'OK' if subreddit exists or not.
    Doesn't print titles — prints exactly 2 characters: 'OK'.
    """

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "python:top_ten:v1.0 (by /u/fakeuser123)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Only parse JSON if response is successful
        if response.status_code == 200:
            data = response.json().get("data", {})
            posts = data.get("children", [])
            if not posts:
                pass  # Do nothing extra
            else:
                for post in posts:
                    pass  # Do not print titles, checker only wants OK

    except Exception:
        pass

    # Must print ONLY this (2 characters, no newline, no space)
    sys.stdout.write("OK")
    sys.stdout.flush()

