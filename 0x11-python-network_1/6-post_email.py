#!/usr/bin/python3
""" Module """


import requests
from sys import argv


if __name__ == "__main__":

    values = {'email': argv[2]}

    req = requests.get(argv[1], param=values)
    print(req.text)
