#!/usr/bin/python3
"""
Module - Myint
"""


class MyInt(int):
    """ int """

    def __eq__(self, other):
        return int(self) != int(other)

    def __ne__(self, other):
        return int(self) == int(other)
