#!/usr/bin/python3
""" Module """


import urllib.request


req = urllib.request.Request('https://intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    print("Body response:")
    print('\t- type: {}'.format(type(response)))
    print('\t- content: {}'.format(response.read()))
    print('\t- utf8 content: {}'.format(response.msg))
