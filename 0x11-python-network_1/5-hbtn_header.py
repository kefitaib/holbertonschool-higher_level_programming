#!/usr/bin/python3
""" Module """


import requests


if __name__ == "__main__":

    req = requests.get("https://intranet.hbtn.io/status")
    print(req.headers['X-Request-Id'])
