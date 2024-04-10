#!/usr/bin/python3
"""Word counter"""
import requests


def count_words(subreddit, word_list, hot_list=None):
    if hot_list is None:
        hot_list = recurse(subreddit)
    if hot_list is None:
        return

    word_count = {}

    for word in word_list:
        word = word.lower()
        count = sum(1 for title in hot_list if f" {word} " in title)
        if count > 0:
            word_count[word] = word_count.get(word, 0) + count

    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_words:
        print(f"{word}: {count}")


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
