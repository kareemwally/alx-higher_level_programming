#!/usr/bin/python3
""" a simple script to fetch some URL"""
import urllib.request


def main():
    """ a script to fetch status of html request"""
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as res:
        content = res.read()
        print("Body response:")
        print("- type: {0}".format(type(content)))
        print("- content: {0}".format(content))
        print("- utf8 content: {0}".format(content.decode('utf-8')))


if __name__ == "__main__":
    main()
