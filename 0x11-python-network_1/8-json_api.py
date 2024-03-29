#!/usr/bin/python3
""" takes in a letter and sends it as a POST request to URL"""

import sys
import requests


if __name__ == "__main__":

    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    data = {"q": letter}
    url = 'http://0.0.0.0:5000/search_user'

    req = requests.post(url, data=data)
    try:
        r = req.json()
        if r == {}:
            print("No result")
        else:
            print(f"[{r.get('id')}] {r.get('name')}")
    except ValueError:
        print("Not a valid JSON")
