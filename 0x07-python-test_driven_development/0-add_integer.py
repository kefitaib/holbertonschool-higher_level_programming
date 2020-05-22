#!/usr/bin/python3
"""

Module - add_integer

"""


def add_integer(a, b=98):
    """
    adds 2 integers
    """
    if a is None or type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)

    if type(b) is float:
        b = int(b)

    return a + b
