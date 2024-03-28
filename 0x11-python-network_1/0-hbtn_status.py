#!/usr/bin/python3
""" a simple script to fetch some URL"""
import urllib.request
with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as res:
    content = res.read()
    print("Body response:")
    print(f"	- type:{type(content)}")
    print(f"	-content:{content}")
    print(f"	-utf8 content:{content.encode('utf-8')}")
