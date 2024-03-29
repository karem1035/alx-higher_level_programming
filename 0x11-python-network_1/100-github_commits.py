#!/usr/bin/python3
""" sends a POST (Email) request to the URL, and displays the body. """
import sys
import requests

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    req = requests.get(url)
    commits = req.json()

    try:
        for i in range(10):
            commit = commits[i]
            ssh = commit.get('sha')
            author = commit.get('commit').get('author').get('name')
            print(f"{ssh}: {author}")
    except IndexError:
        pass
