#!/usr/bin/python3
""" Module """


import requests
from sys import argv


if __name__ == "__main__":

    req = requests.get(argv[1])
    print(req.headers.get('X-Request-Id'))
