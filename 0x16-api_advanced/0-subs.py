#!/usr/bin/python3
""" returns the number of subscribers for a given subreddit. """
import requests


def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    res = requests.get(url)
    if res.status_code != 200:
        return 0
    data = res.json()['data']
    return (data['subscribers'])
