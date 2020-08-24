#!/usr/bin/python3
""" Module """


from urllib import parse
from urllib import request
from sys import argv


if __name__ == "__main__":

    values = {'email' : argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')

    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        print(response.read().decode())
