#!/usr/bin/python3
""" Module """


from urllib.error import URLError
from urllib import request
from sys import argv


if __name__ == "__main__":

    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as response:
            print(response.read().decode())
    except URLError as e:
        print('Error code: ', e.code)
