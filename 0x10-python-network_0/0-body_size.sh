#!/bin/bash
# Prints sizie of the body of the response
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
