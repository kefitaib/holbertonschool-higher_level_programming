#!/usr/bin/python3
""" Module """


from urllib import request
from sys import argv


if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        print(response.headers.['X-Request-Id'])
