#!/usr/bin/python3
""" 0-subs module"""
import requests


def number_of_subscribers(subreddit):
    """ a function that queries the Reddit API and returns the number of
        subscribers (not active users, total subscribers) for a given
        subreddit. If an invalid subreddit is given, the function should
        return 0
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # Set a custom User-Agent to avoid rate limiting
    headers = {'User-Agent': 'my_reddit_api_client'}

    # Make a GET request to the subreddit's info endpoint
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data.get('data').get('subscribers')

    return 0
