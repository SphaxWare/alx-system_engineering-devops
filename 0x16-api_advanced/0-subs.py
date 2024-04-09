#!/usr/bin/python3
"""How many subs"""
import requests


def number_of_subscribers(subreddit):
    """Number of subs"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'ALX-Reddit-Agent'}
    try:
        print(url)
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            subcount = data['data']['subscribers']
            return subcount
        else:
            print(f"Error: {response.status_code}")
            return 0
    except Exception as e:
        print(f"Error: {e}")
        return None
