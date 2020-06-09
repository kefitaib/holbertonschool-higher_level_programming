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

        """  test id"""
        r1 = r(6, 2)
        self.assertAlmostEqual(r1.id, 1)

        r2 = r(2, 3, 3, 2)
        self.assertAlmostEqual(r2.id, 2)

        r3 = r(3, 6, 5, 0, 12)
        self.assertAlmostEqual(r3.id, 12)

        """ test area """
        self.assertAlmostEqual(r1.area(), 12)
        self.assertAlmostEqual(r2.area(), 6)
        self.assertAlmostEqual(r3.area(), 18)

        """ Errors """
        with self.assertRaises(ValueError):
            r4 = r(-12, 10)

        with self.assertRaises(TypeError):
            r5 = r(10, 't')

        with self.assertRaises(TypeError):
            r6 = r(10, 2, 't', 2)

        with self.assertRaises(ValueError):
            r7 = r(10, 2, 6, -2)

        with self.assertRaises(TypeError):
            r7 = r(10, 2, 6, 2, 7, 3)

        with self.assertRaises(TypeError):
            r7 = r(10)

        """ test display """
        s = '######\n######\n'
        self.assertAlmostEqual(r1.display(), print(s))

        s = '\n\n   ##\n   ##\n   ##\n'
        self.assertAlmostEqual(r2.display(), print(s))

        s = '     ###\n     ###\n     ###\n     ###\n     ###\n     ###\n'
        self.assertAlmostEqual(r3.display(), print(s))
