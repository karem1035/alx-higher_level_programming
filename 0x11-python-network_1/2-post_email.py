#!/usr/bin/python3
""" send POST request to the URL with the email, displays the body """
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    req = urllib.request.Request(url, email=email, method='POST')
    with urllib.request.urlopen(req) as response:
        response_content = response.read().decode('utf-8')
        print(response_content)
