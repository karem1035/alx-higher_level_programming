#!/bin/bash
# a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
response=$(curl -s "$1")
response_size=$(echo -n "$response" | wc -c)
echo "$response_size"