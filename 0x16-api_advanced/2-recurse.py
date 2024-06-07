#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests
import requests.auth

CLIENT_ID = "ZHsHCcoQxH9mxjKajUXjYA"
SECRET_KEY = "7KL3Fy26ayJojzjighyIg6OjNI3BMQ"

auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "recurse.py"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False, auth=auth)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
