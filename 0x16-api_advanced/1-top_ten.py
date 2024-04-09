#!/usr/bin/python3
"""Top Ten"""
import requests


def top_ten(subreddit):
    """ first 10 hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'ALX-Reddit-Agent'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()['data']['children']
        if data:
            for post in data[:-1]:
                print(post['data']['title'])
        else:
            print("None")
