#!/usr/bin/python3
"""
Module
"""


def read_file(filename=""):
    """ function """

    with open(filename, encoding='utf8') as f:
        print(f.read(), end="")
