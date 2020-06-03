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

        if isinstance(attrs, list):
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

    def reload_from_json(self, json):

        for k, v in json.items():
            setattr(self, k, v)
