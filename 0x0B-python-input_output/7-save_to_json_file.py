#!/usr/bin/python3
"""
Module
"""


def save_to_json_file(my_obj, filename):
    """ function """

    import json
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
