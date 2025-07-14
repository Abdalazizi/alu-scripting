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
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    # Reddit requires a User-Agent. A descriptive one is good practice.
    headers = {'User-Agent': 'my_custom_reddit_app/1.0'}

    try:
        # Send a GET request to the Reddit API.
        # allow_redirects=False is crucial to avoid following redirects for invalid subreddits.
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            data = response.json()
            # Reddit's API returns a JSON structure. We need to check if 'data'
            # and 'children' keys exist, which signifies a valid subreddit listing.
            if 'data' in data and 'children' in data['data']:
                posts = data['data']['children']
                # Print the title for the first 10 posts found.
                for i, post in enumerate(posts):
                    if i < 10:
                        print(post['data']['title'])
                    else:
                        break  # Stop iterating once 10 titles are printed
            else:
                # If status code is 200 but the JSON structure doesn't match
                # a typical subreddit listing (e.g., it's a search results page),
                # we consider it an invalid subreddit for this task.
                print("None")
        else:
            # If the HTTP status code is not 200 (e.g., 404 Not Found),
            # it indicates an issue or an invalid subreddit.
            print("None")
    except requests.exceptions.RequestException:
        # This catches network-related errors (e.g., no internet connection,
        # DNS resolution failure, connection timeout).
        print("None")
    except ValueError:
        # This catches errors if the response content is not valid JSON,
        # which can happen if the API returns an unexpected format.
        print("None")
    except Exception:
        # A general catch-all for any other unforeseen errors during execution.
        print("None")
