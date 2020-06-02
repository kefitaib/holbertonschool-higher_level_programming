#!/usr/bin/python3
"""
Module - class MyList that inherits from list
"""


class MyList(list):
    """ class represent a new list """

    def print_sorted(self):
        """ sort a list """

        l = self[:]
        l.sort()
        print(l)
