#!/usr/bin/python3
""" empty class Square that defines a square
"""


class Square:
    """ class that define a Square
    """

    def __init__(self, size=0):
        """Initializes the data."""
        self.size = size

    def area(self):
        """ retune the area of the sqaure
        """
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size=0):
        if type(size) is not int or not float:
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = size

    def __lt__(self, other):
        return self.__size * self.__size < other.__size * other.__size

    def __le__(self, other):
        return self.__size * self.__size <= other.__size * other.__size

    def __eq__(self, other):
        return self.__size * self.__size == other.__size * other.__size

    def __ne__(self, other):
        return self.__size * self.__size != other.__size * other.__size

    def __gt__(self, other):
        return self.__size * self.__size > other.__size * other.__size

    def __ge__(self, other):
        return self.__size * self.__size >= other.__size * other.__size
