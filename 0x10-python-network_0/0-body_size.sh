#!/bin/bash
# Prints sizie of the body of the response
response=$(curl -sI "$1")
length=$(echo "$response" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r')
echo "$length"
