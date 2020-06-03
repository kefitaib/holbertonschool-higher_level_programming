#!/usr/bin/python3
"""
Module
"""


def load_from_json_file(filename):
    """ function """

    import json
    with open(filename) as f:
        return json.load(f)
