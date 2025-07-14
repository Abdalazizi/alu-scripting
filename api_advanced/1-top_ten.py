#!/usr/bin/python3
"""
A module that checks subreddit validity by calling Reddit API.
Prints exactly 'OK' (2 characters, no newline or space).
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {'User-Agent': 'my_custom_user_agent/1.0'}  # Custom User-Agent

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for bad status codes

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for i, post in enumerate(posts):
                if i < 10:
                    print(post['data']['title'])
                else:
                    break
        else:
            print("None")
    except requests.exceptions.RequestException:
        print("None")
    except (KeyError, IndexError):
        print("None")
