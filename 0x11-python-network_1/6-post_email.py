#!/usr/bin/python3
""" a simple script to post email using Requests"""
import sys
import requests


def main():
    """ the main function"""
    email = sys.argv[2]
    url = sys.argv[1]
    res = requests.post(url, data={"email": email})


if __name__ == "__main__":
    main()
