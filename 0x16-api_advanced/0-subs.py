#!/usr/bin/python3
""" 0-subs module"""
import requests


def number_of_subscribers(subreddit):
    """ a function that queries the Reddit API and returns the number of
        subscribers (not active users, total subscribers) for a given
        subreddit. If an invalid subreddit is given, the function should
        return 0
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    # Set a custom User-Agent to avoid rate limiting
    headers = {"User-Agent": "0-subs.py"}

    # Make a GET request to the subreddit's info endpoint
    response = requests.get(url, headers=headers, allow_redirects=False)

<<<<<<< HEAD
    if response.status_code <= 200:
=======
    if response.status_code in [200, 302]:
>>>>>>> f0c37f2c014ac02f48266ee77b4d708a0eb784d6
        data = response.json()
        return data.get("data").get("subscribers")

    return 0
