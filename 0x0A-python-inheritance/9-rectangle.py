#!/usr/bin/python3
"""
Module - rectangle
"""


class Rectangle(__import__('7-base_geometry').BaseGeometry):
    """ description of a rectangle """

    def __init__(self, width, height):
        if super().integer_validator("width", width):
            self.__width = width

        if super().integer_validator('height', height):
            self.__height = height

    def area(self):
        """ return the area of the rectangle """

        return self.__width * self.__height

    def __str__(self):
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)
