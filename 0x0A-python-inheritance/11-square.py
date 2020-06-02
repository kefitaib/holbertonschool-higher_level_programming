#!/usr/bin/python3
"""
Module - Square
"""


class Square(__import__('9-rectangle').Rectangle):
    """ description of a square """

    def __init__(self, size):
        if super().integer_validator("size", size):
            self.__size = size

    def area(self):
        """ return the area of the square """

        return self.__size * self.__size

    def __str__(self):
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)
