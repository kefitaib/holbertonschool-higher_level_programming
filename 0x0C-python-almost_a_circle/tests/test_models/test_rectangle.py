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
        """ test value  """

        self.assertAlmostEqual(issubclass(r, b), True)

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

        with self.assertRaises(TypeError) as e:
            msg = "height must be an integer"
            r1 = r(10, 't')

        with self.assertRaises(TypeError) as e:
            msg = "width must be an integer"
            r1 = r(2.5, 't')

        with self.assertRaises(TypeError) as e:
            msg = "x must be an integer"
            r2 = r(10, 2, 't', 2)

        with self.assertRaises(TypeError) as e:
            msg = "y must be an integer"
            r1 = r(10, 2, 3, 'u')

        with self.assertRaises(TypeError) as e:
            msg = '__init__() takes from 3 to 6 positional\
            arguments but 7 were given'
            r3 = r(10, 2, 6, 2, 7, 3)

        with self.assertRaises(TypeError) as e:
            msg = "__init__() missing 1 required positional argument: 'height'"
            r4 = r(10)

        self.assertAlmostEqual(msg, str(e.exception))

    def test_Value(self):
        """ Error """

        with self.assertRaises(ValueError) as e:
            msg = 'width must be > 0'
            r1 = r(-12, 10)

        with self.assertRaises(ValueError) as e:
            msg = 'height must be > 0'
            r1 = r(12, -10)

        with self.assertRaises(ValueError) as e:
            msg = 'y must be >= 0'
            r1 = r(10, 2, 6, -2)

        with self.assertRaises(ValueError) as e:
            msg = 'x must be >= 0'
            r1 = r(12, 10, -6, 3)

        self.assertAlmostEqual(msg, str(e.exception))

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

    def test_Str(self):
        """ str """

        r1 = r(4, 6, 2, 1, 12)
        s = '[Rectangle] (12) 2/1 - 4/6'
        self.assertAlmostEqual(print(r1), print(s))

        r2 = r(5, 5, 1)
        s = '[Rectangle] (1) 1/0 - 5/5'
        self.assertAlmostEqual(print(r2), print(s))

    def test_Update(self):
        """ update """

        r1 = r(10, 10, 10, 10)
        s = '[Rectangle] (1) 10/10 - 10/10'
        self.assertAlmostEqual(print(r1), print(s))

        r1.update(89)
        s = '[Rectangle] (89) 10/10 - 10/10'
        self.assertAlmostEqual(print(r1), print(s))

        r1.update(89, 2)
        s = '[Rectangle] (89) 10/10 - 2/10'
        self.assertAlmostEqual(print(r1), print(s))

        r1.update(89, 2, 3)
        s = "[Rectangle] (89) 10/10 - 2/3"
        self.assertAlmostEqual(print(r1), print(s))

        r1.update(89, 2, 3, 4)
        s = "[Rectangle] (89) 4/10 - 2/3"
        self.assertAlmostEqual(print(r1), print(s))

        r1.update(89, 2, 3, 4, 5)
        s = "[Rectangle] (89) 4/5 - 2/3"
        self.assertAlmostEqual(print(r1), print(s))

    def test_Update2(self):
        """ update """

        r1 = r(10, 10, 10, 10)
        s = '[Rectangle] (1) 10/10 - 10/10'
        self.assertAlmostEqual(print(r1), print(s))

        r1.update(height=1)
        s = '[Rectangle] (1) 10/10 - 10/1'
        self.assertAlmostEqual(print(r1), print(s))

        r1.update(width=1, x=2)
        s = '[Rectangle] (1) 2/10 - 1/1'
        self.assertAlmostEqual(print(r1), print(s))

        r1.update(y=1, width=2, x=3, id=89)
        s = "[Rectangle] (89) 10/10 - 2/3"
        self.assertAlmostEqual(print(r1), print(s))

        r1.update(x=1, height=2, y=3, width=4)
        s = "[Rectangle] (89) 1/3 - 4/2"
        self.assertAlmostEqual(print(r1), print(s))
