#!/usr/bin/python3
"""
Module
"""


def append_write(filename="", text=""):
    """ function """

    with open(filename, 'a', encoding='utf8') as f:
        return f.write(text)
