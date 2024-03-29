#!/usr/bin/python3
""" a simple script to fetch some URL"""
import urllib.request
import sys

def main():
    """ a script to fetch status of html request"""
    with urllib.request.urlopen(sys.argv[1]) as res:
        content = res.getheader("X-Request-Id")
        print("{0}".format(res.header))


if __name__ == "__main__":
    main()
