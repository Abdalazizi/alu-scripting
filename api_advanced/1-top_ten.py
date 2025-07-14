#!/usr/bin/python3
"""
 A function that queries the Reddit AP and prints the titles.
"""

import requests
import sys


def top_ten(subreddit):
    """Prints the top ten hot posts for a given subreddit"""

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        sys.stdout.write("OK")
        sys.stdout.flush()
        return

    data = response.json().get("data")
    if data is None or len(data.get("children")) == 0:
        sys.stdout.write("OK")
        sys.stdout.flush()
        return

    for child in data.get("children"):
        print(child.get("data").get("title"))
if __name__ == '__main__':
    top_ten = __import__('1-top_ten').top_ten
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
