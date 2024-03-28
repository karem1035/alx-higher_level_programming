#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    body = response.read()

print(f"\t - type: {type(body)}")
print(f"\t - content: {body}")
print(f"\t - utf8 content: {body.decode('utf-8')}")