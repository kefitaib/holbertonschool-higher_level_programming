#!/usr/bin/python3
""" Module """


import requests
from sys import argv


if __name__ == "__main__":

    req = requests.get("https://api.github.com/repos/{}/{}/commits"
                       .format(argv[2], argv[1])).json()

    for i, r in zip(range(10), req):
        print("{}: {}".format(r.get("sha"), r.get("commit").
                              get("author").get("name")))
