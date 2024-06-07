#!/usr/bin/python3
""" 0-subs module"""
import requests
import requests.auth

CLIENT_ID = "ZHsHCcoQxH9mxjKajUXjYA"
SECRET_KEY = "7KL3Fy26ayJojzjighyIg6OjNI3BMQ"

auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)


def number_of_subscribers(subreddit):
    """ a function that queries the Reddit API and returns the number of
        subscribers (not active users, total subscribers) for a given
        subreddit. If an invalid subreddit is given, the function should
        return 0
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    # Set a custom User-Agent to avoid rate limiting
    headers = {'User-Agent': '0-subs.py'}

    # Make a GET request to the subreddit's info endpoint
    response = requests.get(
            url, headers=headers, allow_redirects=False,
            auth=auth)

    if response.status_code == 200:
        data = response.json()
        return data.get('data').get('subscribers')

    return 0
