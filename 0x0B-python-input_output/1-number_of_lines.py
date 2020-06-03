#!/usr/bin/python3
"""
Module
"""


def number_of_lines(filename=""):
    """ fonction """

    with open(filename, encoding='utf8') as f:
        return len(f.readlines())
