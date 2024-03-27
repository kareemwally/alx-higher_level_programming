#!/bin/bash
#getting a body of http
curl -s -o /blah -w "%{http_code}" "$1" | grep -q 200 && curl -s "$1"
