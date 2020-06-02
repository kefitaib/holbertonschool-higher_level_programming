#!/usr/bin/python3
"""
Module - BaseGeometry
"""


class BaseGeometry():
    """ class defenition of BaseGeometry """

    def area(self):
        """ return the area """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """

        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

        return True
