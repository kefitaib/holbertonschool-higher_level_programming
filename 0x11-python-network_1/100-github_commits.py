#!/usr/bin/python3
""" Module """


import requests
from sys import argv


if __name__ == "__main__":

    req = requests.get("https://api.github.com/repos/{}/{}/commits"
                       .format(argv[2], argv[1])).json()

    i = 0
    try:
        while i < 10:
            print("{}: {}".format(req[i]['sha'],
                                  req[i]['commit']['author']['name']))
        i += 1
    except:
        pass
