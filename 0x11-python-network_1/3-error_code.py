#!/usr/bin/python3
""" sends a request to the URL and displays the body (decoded in utf-8). """
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            response_content = response.read().decode('utf-8')
            print(response_content)
    except urllib.error.HTTPError as error:
        print(f"Error code: {error.code}")
