#!/usr/bin/python3
""" a simple script to fetch some URL"""
import urllib.request
with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as res:
    html = res.read()
    print(html)
