#!/usr/bin/python3
import math


class MagicClass:
    def __init__(self, radius):
        if type(radius) is not int or not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        return self.__radius * math.pi * 2
