#!/usr/bin/python3
"""
Module - test unit file
"""


import unittest
from models.rectangle import Rectangle as r


class TestBade(unittest.TestCase):
    """ class test """

    def test_Init(self):
        """ test value  """

        r1 = r(6, 2)
        self.assertAlmostEqual(r1.x, 0)
        self.assertAlmostEqual(r1.y, 0)
        self.assertAlmostEqual(r1.width, 6)
        self.assertAlmostEqual(r1.height, 2)

        r2 = r(2, 3, 3, 2)
        self.assertAlmostEqual(r2.y, 2)
        self.assertAlmostEqual(r2.x, 3)
        self.assertAlmostEqual(r2.width, 2)
        self.assertAlmostEqual(r2.height, 3)

        r3 = r(3, 6, 5, 0, 12)
        self.assertAlmostEqual(r3.id, 12)
        self.assertAlmostEqual(r3.x, 5)
        self.assertAlmostEqual(r3.y, 0)
        self.assertAlmostEqual(r3.width, 3)
        self.assertAlmostEqual(r3.height, 6)

    def test_Type(self):
        """ Errors """

        with self.assertRaises(TypeError):
            ex = " must be an integer"
            r1 = r(10, 't')

        with self.assertRaises(TypeError):
            r2 = r(10, 2, 't', 2)

        with self.assertRaises(TypeError):
            r3 = r(10, 2, 6, 2, 7, 3)

        with self.assertRaises(TypeError):
            r4 = r(10)

    def test_Value(self):
        """ Error """

        with self.assertRaises(ValueError):
            r1 = r(-12, 10)

        with self.assertRaises(ValueError):
            r1 = r(10, 2, 6, -2)

    def test_Area(self):
        """ test area """

        r1 = r(6, 2)
        self.assertAlmostEqual(r1.area(), 12)

        r2 = r(2, 3, 3, 2)
        self.assertAlmostEqual(r2.area(), 6)

        r3 = r(3, 6, 5, 0, 12)
        self.assertAlmostEqual(r3.area(), 18)

    def test_Display(self):
        """ test display """

        r1 = r(6, 2)
        s = '######\n######\n'
        self.assertAlmostEqual(r1.display(), print(s))

        r2 = r(2, 3, 3, 2)
        s = '\n\n   ##\n   ##\n   ##\n'
        self.assertAlmostEqual(r2.display(), print(s))

        r3 = r(3, 6, 5, 0, 12)
        s = '     ###\n     ###\n     ###\n     ###\n     ###\n     ###\n'
        self.assertAlmostEqual(r3.display(), print(s))
