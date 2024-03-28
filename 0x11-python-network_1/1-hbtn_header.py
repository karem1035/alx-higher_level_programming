#!/usr/bin/python3
""" prints X-Request-Id variable found in the header. """
import sys
import urllib.request

url = sys.argv[1]
response = urllib.request.urlopen(url)

print(response.headers.get('X-Request-Id'))
