#!/usr/bin/python3
"""
Module
"""


class Student():
    """ class description """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        if attrs:
            d = {}
            for i in attrs:
                if hasattr(self, i):
                    d[i] = self.__dict__[i]

            return d

        return self.__dict__
