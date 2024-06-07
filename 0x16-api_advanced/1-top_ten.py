#!/usr/bin/python3
""" 1.top_ten module"""

import requests
import requests.auth

CLIENT_ID = "ZHsHCcoQxH9mxjKajUXjYA"
SECRET_KEY = "7KL3Fy26ayJojzjighyIg6OjNI3BMQ"

auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)


def top_ten(subreddit):
    """  a function that queries the Reddit API and prints the titles of the
         first 10 hot posts listed for a given subreddit.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "1-top_ten"}
    response = requests.get(
            url, headers=headers, allow_redirects=False, auth=auth)

    if response.status_code == 200:
        data = response.json()
        for i, child in enumerate(data.get('data', {}).get('children', [])):
            if i >= 10:
                break
            print(child.get('data', {}).get('title'))
    else:
        print("None")
