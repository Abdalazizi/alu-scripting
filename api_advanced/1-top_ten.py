#!/usr/bin/python3
"""
This module provides a function to query the Reddit API
and print the titles of the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the top 10 hot posts for a given subreddit.
    If the subreddit is invalid or an error occurs, prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'my_custom_reddit_app/1.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'children' in data['data']:
                posts = data['data']['children']
                for i, post in enumerate(posts[:10]):
                    print(post['data']['title'])
            else:
                print(None)
        else:
            print(None)

    except requests.exceptions.RequestException:
        print(None)
    except ValueError:
        print(None)
    except Exception:
        print(None)

