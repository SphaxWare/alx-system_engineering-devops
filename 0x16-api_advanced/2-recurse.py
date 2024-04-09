#!/usr/bin/python3
"""Top articles"""
import requests


def recurse(subreddit, hot_list=[]):
    """list containing the titles of all hot articles"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'ALX-Reddit-Agent'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()['data']['children']
        if data:
            for post in data:
                hot_list.append(post['data']['title'])
            return hot_list
        else:
            return None
