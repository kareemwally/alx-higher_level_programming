#!/usr/bin/python3
"""Fetching the response body from a URL using the requests package"""
import requests
import sys


def main():
    """Get the response body from the URL"""
    try:
        url = sys.argv[1]
        response = requests.get(url)
        if response.status_code >= 400:
            print("Error code: {0}".format(response.status_code))
        else:
            print(response.text)
    except IndexError:
        print("Usage: python script.py <URL>")


if __name__ == "__main__":
    main()
