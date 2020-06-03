#!/usr/bin/python3
"""
Module
"""


def read_lines(filename="", nb_lines=0):
    """ fonction """

    with open(filename, encoding='utf8') as f:
        x = len(f.readlines())

        f.seek(0)
        if nb_lines <= 0 or nb_lines >= x:
            print(f.read(), end="")

        else:
            for i in range(nb_lines):
                print(f.readline(), end="")
