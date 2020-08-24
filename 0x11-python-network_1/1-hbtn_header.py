#!/usr/bin/python3
""" Module """


from urllib import request
from sys import argv


req = request.Request(argv[1])
with request.urlopen(req) as response:
    html = response.headers
    print(html['X-Request-Id'])

    #print("Body response:")
    #print('\t- type: {}'.format(type(html)))
    #print('\t- content: {}'.format(html))
    #print('\t- utf8 content: {}'.format(html.decode('utf-8')))
