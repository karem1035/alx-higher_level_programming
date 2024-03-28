#!/usr/bin/python3
""" sends a request to the URL and displays the body (decoded in utf-8). """
import sys
import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')
    print("Body response:")
    print(f"\t- type: {type(data)}")
    print(f"\t- content: {data}")
