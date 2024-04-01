#!/usr/bin/python3
""" a python script to get a specific data"""
import requests
import sys


def main():
    """ getting a specific params"""
    res = requests.get(sys.argv[1])
    res_dict = res.json()
    print(res_dict["X-Request-Id"])


if __name__ == "__main__":
    main()
