#!/usr/bin/python3
""" a simple script to send request"""
import sys
import requests


def main():
    """ the main function"""
    try:
        url = sys.argv[1]
        res = requests.get(url)
        res.raise_for_status()
        print(res.text)
    except requests.exceptions.HTTPError as http_err:
        print("Error code:".format(res.status_code))


if __name__ == "__main__":
    main()
