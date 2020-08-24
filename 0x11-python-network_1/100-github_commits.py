#!/usr/bin/python3
""" Module """


import requests
from sys import argv


if __name__ == "__main__":

    req = requests.get("https://api.github.com/repos/{}/{}/commits"
                       .format(argv[2], argv[1])).json()

    i = 0
    while i < 10:
        if req[i]:
            print("{}: {}".format(req[i].get("sha"), req[i].get("commit").
                                  get("author").get("name")))
        else:
            break

        i += 1
