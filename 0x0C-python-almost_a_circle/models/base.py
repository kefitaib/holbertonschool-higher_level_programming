#!/usr/bin/python3
"""
Module - class
"""


import json
import os.path as o


class Base():
    """ class base"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """

        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return '[]'

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """

        with open(cls.__name__ + ".json", 'w') as f:
            l = []
            if list_objs is None or len(list_objs) <= 0:
                f.write(Base.to_json_string(l))

            else:
                for obj in list_objs:
                    l.append(cls.to_dictionary(obj))
                f.write(Base.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """

        l = []
        if json_string is None or len(json_string) <= 0:
            return l

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """

        if cls.__name__ == 'Rectangle':
            rec = cls(2, 3)

        else:
            rec = cls(2)

        rec.update(**dictionary)
        return rec

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """

        l = []
        if o.exists(cls.__name__ + ".json"):
            with open(cls.__name__ + ".json") as f:
                for line in f:
                    s = cls.from_json_string(line)
                    for d in s:
                        l.append(cls.create(**d))

        return l
