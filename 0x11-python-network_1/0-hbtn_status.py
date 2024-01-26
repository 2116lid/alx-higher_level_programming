#!/usr/bin/python3
"""A module to fetchurl"""
import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as rep:
    fet = rep.read()
print("Body response:\n\t- type: {}".format(type(fet)))
print('\t- content: {}'.format(fet))
print('\t- utf8 content: {}'.format(fet.decode('utf-8')))
