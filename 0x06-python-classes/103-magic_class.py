#!/usr/bin/python3
"""MagicClass"""
import math


class MagicClass:
    """MagicClass"""
    def __init__(self, radius=0):
        if type(radius) is not int or not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        return self.__radius * math.pi * 2
