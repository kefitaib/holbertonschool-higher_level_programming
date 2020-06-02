#!/usr/bin/python3
"""
Module - function
"""


def add_attribute(obj, attr, val):
    """ set attribute """

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, val)
