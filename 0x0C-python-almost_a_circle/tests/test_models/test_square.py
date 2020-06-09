#!/usr/bin/python3
"""
Module - test unit file
"""


import unittest
from models.rectangle import Rectangle as r
from models.square import Square as s


class TestSquare(unittest.TestCase):
    """ class test """

    def test_Init(self):
        """ test value  """

        self.assertTrue(issubclass(s, r))

        s1 = s(6)
        self.assertAlmostEqual(s1.x, 0)
        self.assertAlmostEqual(s1.y, 0)
        self.assertAlmostEqual(s1.width, 6)
        self.assertAlmostEqual(s1.height, 6)

        s2 = s(2, 3)
        self.assertAlmostEqual(s2.y, 0)
        self.assertAlmostEqual(s2.x, 3)
        self.assertAlmostEqual(s2.width, 2)
        self.assertAlmostEqual(s2.height, 2)

        s3 = s(3, 6, 5, 12)
        self.assertAlmostEqual(s3.id, 12)
        self.assertAlmostEqual(s3.x, 6)
        self.assertAlmostEqual(s3.y, 5)
        self.assertAlmostEqual(s3.width, 3)
        self.assertAlmostEqual(s3.height, 3)

    def test_Type(self):
        """ Errors """

        with self.assertRaises(TypeError) as e:
            msg = "width must be an integer"
            s1 = s('t')

        with self.assertRaises(TypeError) as e:
            msg = "x must be an integer"
            s2 = s(10, 't')

        with self.assertRaises(TypeError) as e:
            msg = "y must be an integer"
            s3 = s(10, 2, 'u')

        with self.assertRaises(TypeError) as e:
            msg = '__init__() takes from 2 to 5 positional arguments\
            but 6 were given'
            s4 = s(10, 2, 6, 2, 3)

        with self.assertRaises(TypeError) as e:
            msg = "__init__() missing 1 required positional argument: 'size'"
            s5 = s()

        self.assertAlmostEqual(msg, str(e.exception))

    def test_Value(self):
        """ Error """

        with self.assertRaises(ValueError) as e:
            msg = 'width must be > 0'
            s1 = s(-12)

        with self.assertRaises(ValueError) as e:
            msg = 'y must be >= 0'
            s1 = s(10, 2, -6)

        with self.assertRaises(ValueError) as e:
            msg = 'x must be >= 0'
            s1 = s(12, -10, 6)

        self.assertAlmostEqual(msg, str(e.exception))

    def test_Area(self):
        """ test area """

        s1 = s(6)
        self.assertAlmostEqual(s1.area(), 36)

        s2 = s(2, 3)
        self.assertAlmostEqual(s2.area(), 4)

        s3 = s(3, 6, 5)
        self.assertAlmostEqual(s3.area(), 9)

    def test_Display(self):
        """ test display """

        s1 = s(6)
        m = '######\n######\n######\n######\n######\n######\n'
        self.assertAlmostEqual(s1.display(), print(m))

        s2 = s(2, 3)
        m = '   ##\n   ##\n'
        self.assertAlmostEqual(s2.display(), print(m))

        s3 = s(3, 6, 5)
        m = '\n\n\n\n\n      ###\n      ###\n      ###\n'
        self.assertAlmostEqual(s3.display(), print(m))

    def test_Str(self):
        """ str """

        s1 = s(5)
        m = '[Square] (1) 0/0 - 5'
        self.assertAlmostEqual(print(s1), print(m))

        s2 = s(2, 2)
        m = '[Square] (2) 2/0 - 2'
        self.assertAlmostEqual(print(s2), print(m))

        s3 = s(3, 1, 3)
        m = '[Square] (3) 1/3 - 3'
        self.assertAlmostEqual(print(s3), print(m))

    def test_Size(self):
        """ test """

        s1 = s(5)
        m = '[Square] (1) 0/0 - 5'
        self.assertAlmostEqual(print(s1), print(m))
        self.assertAlmostEqual(s1.size, 5)

        s1.size = 10
        m = '[Square] (1) 0/0 - 10'
        self.assertAlmostEqual(print(s1), print(m))
        self.assertAlmostEqual(s1.size, 10)

    def test_Update(self):
        """ update """

        s1 = s(5)
        m = '[Square] (1) 0/0 - 5'
        self.assertAlmostEqual(print(s1), print(m))

        s1.update(10)
        m = '[Square] (10) 0/0 - 5'
        self.assertAlmostEqual(print(s1), print(m))

        s1.update(1, 2)
        m = '[Square] (1) 0/0 - 2'
        self.assertAlmostEqual(print(s1), print(m))

        s1.update(1, 2, 3)
        m = "[Square] (1) 3/0 - 2"
        self.assertAlmostEqual(print(s1), print(m))

        s1.update(1, 2, 3, 4)
        m = "[Square] (1) 3/4 - 2"
        self.assertAlmostEqual(print(s1), print(m))

        s1.update(x=12)
        m = "[Square] (1) 12/4 - 2"
        self.assertAlmostEqual(print(s1), print(m))

        s1.update(size=7, y=1)
        m = "[Square] (1) 12/1 - 7"
        self.assertAlmostEqual(print(s1), print(m))

        s1.update(size=7, id=89, y=1)
        m = "[Square] (89) 12/1 - 7"
        self.assertAlmostEqual(print(s1), print(m))

    def test_dict(self):
        """ test """

        s1 = s(10, 2, 1)
        s1_d = s1.to_dictionary()
        m = "{'id': 1, 'x': 2, 'size': 10, 'y': 1} "
        self.assertAlmostEqual(len(str(s1_d)), len(m))
        self.assertAlmostEqual(str(type(s1_d)), "<class 'dict'>")
