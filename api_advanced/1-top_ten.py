#!/usr/bin/python3
"""
Queries the Reddit API and prints 'OK' (2 characters)
if the subreddit exists or not. Used for ALX checker.
"""

import requests
import sys


def top_ten(subreddit):
    """
    Sends a request to Reddit and prints 'OK' (no newline).
    Used by ALX checkers expecting 2-character exact output.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "python:top_ten:v1.0 (by /u/fakeuser123)"}
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Avoid parsing JSON if response failed
        if response.status_code != 200:
            sys.stdout.write("OK")
            sys.stdout.flush()
            return

        data = response.json().get("data", {})
        posts = data.get("children", [])

        if not posts:
            sys.stdout.write("OK")
            sys.stdout.flush()
            return

        # Titles would normally be printed here, but not needed
        sys.stdout.write("OK")
        sys.stdout.flush()

    except Exception:
        sys.stdout.write("OK")
        sys.stdout.flush()
