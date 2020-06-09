#!/usr/bin/python3
"""
Module - test unit file
"""


import unittest
from models.base import Base as b
from models.rectangle import Rectangle as r


class TestBade(unittest.TestCase):
    """ class test """

    def test_Init(self):
        """ test valu """

        b1 = b()
        self.assertAlmostEqual(b1.id, 1)

        b2 = b()
        self.assertAlmostEqual(b2.id, 2)

        b3 = b(12)
        self.assertAlmostEqual(b3.id, 12)

        b4 = b()
        self.assertAlmostEqual(b4.id, 3)

    def test_json(self):
        """ json convert """

        r1 = r(10, 7, 2, 8)
        d = r1.to_dictionary()
        j_d = b.to_json_string([d])
        s = "{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}"
        self.assertAlmostEqual(print(d), print(s))
        self.assertAlmostEqual(print(type(d)), print("<class 'dict'>"))
        s = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        self.assertAlmostEqual(print(j_d), print(s))
        self.assertAlmostEqual(print(type(j_d)), print("<class 'str'>"))

    def test_json_to_file(self):
        """ save to file """

        r1 = r(10, 7, 2, 8)
        r2 = r(2, 4)
        r.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            s = '[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}\
            ,{"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]'
            self.assertAlmostEqual(print(file.read()), print(s))

    def test_json_to_dict(self):
        """  to dict """

        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]

        j = r.to_json_string(list_input)
        lo = r.from_json_string(j)
        s = "<class 'list'>"
        self.assertAlmostEqual(print(type(list_input)), print(s))
        s = "[{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1\
        , 'id': 7}]"
        self.assertAlmostEqual(print(list_input), print(s))

        s = "<class 'str'>"
        self.assertAlmostEqual(print(type(j)), print(s))
        s = '[{"height": 4, "width": 10, "id": 89},\
        {"height": 7, "width": 1, "id": 7}]'
        self.assertAlmostEqual(print(j), print(s))

        s = "<class 'list'>"
        self.assertAlmostEqual(print(type(lo)), print(s))
        s = "self.assertAlmostEqual(print(type(list_input)), print(s))"
        self.assertAlmostEqual(print(lo), print(s))

    def test_dict_to_instance(self):
        """ dict to instance """

        r1 = r(3, 5, 1)
        d = r1.to_dictionary()
        r2 = r.create(**d)
        s = '[Rectangle] (1) 1/0 - 3/5'
        self.assertAlmostEqual(print(r1), print(s))
        self.assertAlmostEqual(print(r2), print(s))
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)
