#!/usr/bin/python3
"""Top articles"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """list containing the titles of all hot articles"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'ALX-Reddit-Agent'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()['data']['children']
        if data:
            for post in data:
                hot_list.append(post['data']['title'])
            after = data[-1]['data']['name']
            return recurse(subreddit, hot_list, after)
        else:
            if len(hot_list) == 0:
                return None
            return hot_list
    else:
        return None
