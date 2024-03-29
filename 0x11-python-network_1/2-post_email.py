#!/usr/bin/python3
""" a simple script to fetch some URL"""
import urllib.request
import sys


def main():
    """ a script to fetch status of html request"""
    email = sys.argv[2]
    data = urlib.parse.urlencode({"email": email}).encode("utf-8")
    with urllib.request.urlopen(sys.argv[1], data=data) as res:
        content = res.read().decode("utf-8")
        print("Your email is: {0}".format(content))


if __name__ == "__main__":
    main()
