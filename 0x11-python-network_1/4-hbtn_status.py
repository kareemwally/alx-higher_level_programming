#!/usr/bin/python3
"""fetching URLs using Requests module"""
import requests


def Request_fetch():
    """ a function to fetch urls"""
    req = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('	- type: {0}'.format(type(req.text)))
    print('	- content: {0}'.format(req.content.decode('utf-8')))


if __name__ == "__main__":
    Request_fetch()
