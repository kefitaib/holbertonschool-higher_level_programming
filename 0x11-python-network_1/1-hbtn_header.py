#!/usr/bin/python3
""" Module """


from urllib import request
from sys import argv


if __name__ == "__main__":
    req = request.Request(argv[1])
    with request.urlopen(req) as response:
        print(response.headers['X-Request-Id'])
