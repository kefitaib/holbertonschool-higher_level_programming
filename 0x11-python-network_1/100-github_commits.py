#!/usr/bin/python3
""" Module """


import requests
from sys import argv


if __name__ == "__main__":

    req = get("https://api.github.com/repos/{}/{}/commits"
              .format(argv[2], argv[1])).json()

    i = 0
    while i < 10:
        print("{}: {}".format(res[i]['sha'], res[i]['committer'][0]))
        i += 1
