#!/bin/bash
# getting the response status_code
curl -s -o null -w "%w{http_code}" "$1"
