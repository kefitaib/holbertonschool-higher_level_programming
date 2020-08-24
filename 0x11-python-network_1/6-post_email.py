#!/usr/bin/python3
""" Module """


import requests
from sys import argv


if __name__ == "__main__":

    values = {'email': argv[2]}

    req = requests.post(argv[1], params=values)
    print(req.text)
