#!/bin/bash
# Send a cURL request and store the response in a temporary file
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
