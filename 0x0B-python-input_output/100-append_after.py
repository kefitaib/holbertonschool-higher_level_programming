#!/usr/bin/python3
"""
Module
"""


def append_after(filename="", search_string="", new_string=""):
    """ function """

    with open(filename, 'r+') as f:
        s = ""
        for l in f:
            s += l
            if search_string in l:
                s += new_string

        f.seek(0)
        f.truncate()
        f.write(s)
