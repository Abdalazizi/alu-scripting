#!/usr/bin/python3
"""
Module to fetch subreddit information from Reddit API.
Includes number of subscribers and subreddit rules.
"""

import requests
import json


def get_subreddit_info_json(subreddit):
    """
    Returns the number of subscribers and rules for a given subreddit.
    If subreddit is invalid, prints an error and returns None.
    """
    headers = {'User-Agent': 'RedditInfoScript/0.1 by YourUsername'}

    # Reddit API endpoints
    about_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    rules_url = f"https://www.reddit.com/r/{subreddit}/about/rules.json"

    # Make requests
    about_resp = requests.get(about_url, headers=headers)
    rules_resp = requests.get(rules_url, headers=headers)

    if about_resp.status_code != 200 or rules_resp.status_code != 200:
        print(json.dumps({"error": "Failed to fetch subreddit data"}, indent=4))
        return

    # Parse data
    about_data = about_resp.json()['data']
    rules_data = rules_resp.json()['rules']

    # Create JSON output
    output = {
        "Name Of Subreddit": about_data['display_name_prefixed'],
        "Subscriber Count": about_data['subscribers'],
        "Description": about_data['public_description'],
        "Rules": [rule['short_name'] for rule in rules_data]
    }

    # Print as pretty JSON
    print(json.dumps(output, indent=4))

# Example usage
get_subreddit_info_json("python")


