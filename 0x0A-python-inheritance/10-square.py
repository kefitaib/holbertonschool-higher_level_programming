#!/usr/bin/python3
"""
Module - Square
"""


class Square(__import__('9-rectangle').Rectangle):
    """ description of a square """

    def __init__(self, size):
        super().__init__(size, size)

    def area(self):
        """ return the area of the square """

        return super().area()

    def __str__(self):
        return super().__str__()
