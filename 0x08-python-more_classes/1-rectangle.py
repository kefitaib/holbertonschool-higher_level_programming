#!/usr/bin/python3
"""
Module - Class Rectangle
"""


class Rectangle:
    """
    class - define a rectangle
    """

    def __init__(self, width=0, height=0):
        """ init finction """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ get the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the width """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ get the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set the height """
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
