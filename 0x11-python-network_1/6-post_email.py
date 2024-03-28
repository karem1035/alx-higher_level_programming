#!/usr/bin/python3
""" sends a POST (Email) request to the URL, and displays the body. """
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    req = requests.post(url, data=value)
