#!/usr/bin/python
"""

test unit file that test a max integer in a list

"""


import unittest
max_integer = __import__('6-max_integer'). max_integer


class Testmaxlist(unittest.TestCase):
    """
    class for test
    """

    def test_max(self):
        """
        test a valide cases
        """

        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([1, 10, 3, 4]), 10)
        self.assertAlmostEqual(max_integer([16, 2, 3, 4]), 16)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([-3, -8, -20]), -3)

    def test_Type(self):
        """
        test value
        """

        self.assertRaises(TypeError, max_integer, [1, 2, 3, 'T'])
        self.assertRaises(TypeError, max_integer, [1, 2, 3, [6, 5]])
        self.assertRaises(TypeError, max_integer, [1, 2, 3, "hi"])
        self.assertRaises(TypeError, max_integer, None)
