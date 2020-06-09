#!/usr/bin/python3
"""
Module - test unit file
"""


import unittest
from models.base import Base as b


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
