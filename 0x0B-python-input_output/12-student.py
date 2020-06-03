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
            if any(not isinstance(i, str) for i in attrs):
                return self.__dict__

            else:
                d = {}
                for i in attrs:
                    if hasattr(self, i):
                        d[i] = str(getattr(self, i))

                return d

        else:
            return self.__dict__
