#!/usr/bin/python3
"""Fetching a specific data from a URL using the requests package"""
import requests
import sys


def main():
    """Get the value of X-Request-Id from the response header"""
    try:
        url = sys.argv[1]
        response = requests.get(url)
        x_request_id = response.headers.get("X-Request-Id")
        if x_request_id:
            print("{0}".format(x_request_id))
        else:
            print("X-Request-Id not found in the response headers.")
    except IndexError:
        print("Usage: python script.py <URL>")


if __name__ == "__main__":
    main()
