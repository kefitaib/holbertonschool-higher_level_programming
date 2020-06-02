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
