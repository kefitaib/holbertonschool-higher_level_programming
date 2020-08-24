#!/usr/bin/python3
""" Module """


import requests
from sys import argv
from requests.exceptions import HTTPError


if __name__ == "__main__":

    values = {'q': ""}
    if len(argv) == 2:
        values['q'] = argv[1]

        req = requests.post('http://0.0.0.0:5000/search_user', data=values)
        try:
            if not req.json():
                print("No result")

            else:
                print("[{}] {}".format(req.json().get('id'),
                                       req.json().get('name')))

        except:
            print("Not a valid JSON")
