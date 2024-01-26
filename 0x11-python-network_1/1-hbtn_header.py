#!/usr/bin/python3
"""A module to takes in a URL, sends a request to the URL and display it"""
import urllib.request
import sys


req = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(req) as rep:
    print(rep.headers.get("X-Request-Id"))
