#!/usr/bin/python3
""" Module """


import requests
from sys import argv


if __name__ == "__main__":

    req = requests.get("https://api.github.com/repos/{}/{}/commits"
                       .format(argv[2], argv[1])).json()

    i = 0
    for i, r in enumerate(req):
        print("{}: {}".format(r.get("sha"), r.get("commit").
                              get("author").get("name")))
        if i == 9:
            break

        i += 1
