#!/usr/bin/python3
"""
Module
"""


def append_after(filename="", search_string="", new_string=""):
    """ function """

    s = ""
    with open(filename, 'r+') as f:
        for l in f:
            s += l
            if search_string in l:
                s += new_string

        f.truncate(0)
        f.write(s)
