#!/usr/bin/python3
# a function that queries the Reddit API and returns the number of subscribers
# (not active users, total subscribers) for a given subreddit. If an invalid
# subreddit is given, the function should return 0.

import requests


def number_of_subscribers(subreddit):

    link = f"https://www.reddit.com/r/{subreddit}/about.json"
    try:
        # Set a custom User-Agent to avoid rate limiting
        headers = {'User-Agent': 'my_reddit_api_client'}

        # Make a GET request to the subreddit's info endpoint
        response = requests.get(link, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except (requests.exceptions.RequestException, KeyError):
        return 0
