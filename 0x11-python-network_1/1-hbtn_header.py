#!/usr/bin/python3
""" prints X-Request-Id variable found in the header. """
import sys
import urllib.request
if __name__ == "__main__":
    url = sys.argv[1]
    response = urllib.request.urlopen(url)
    print(dict(response.headers).get('X-Request-Id'))
