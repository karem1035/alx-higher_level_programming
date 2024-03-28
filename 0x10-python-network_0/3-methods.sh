#!/bin/bash
# can take URL and displays all HTTP methods the server will accept in
curl -sI "$1" | grep "Allow: " | cut -d' ' -f 2-
