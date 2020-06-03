#!/usr/bin/python3
"""
Module
"""


def number_of_lines(filename=""):
    """ fonction """

    x = 0
    with open(filename, encoding='utf8') as f:
        for l in f:
            x += 1

    return x
