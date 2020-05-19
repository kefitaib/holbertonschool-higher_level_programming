#!/usr/bin/python3
""" empty class Square that defines a square
"""


class Square:
    """ class that define a Square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data."""
        self.__size = size

        if type(position) is not tuple or len(position) != 2 or\
           type(position[0]) is not int or position[0] < 0 or\
           type(position[1]) is not int or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """ retune the area of the sqaure
        """
        return self.__size * self.__size

    @property
    def size(self):
        """gat a sqaure"""
        return self.__size

    @size.setter
    def size(self, size=0):
        """set a size for the square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = size

    def my_print(self):
        """print a sqaure"""

        if self.__size == 0:
            print()

        else:
            for i in range(self.__position[1]):
                print()

            for i in range(self.__size):
                for j in range(self.__size + self.__position[0]):
                    if j < self.__position[0]:
                        print(" ", end="")
                    else:
                        print("#", end="")
                print()

    @property
    def position(self):
        """get a square"""
        return self.__position

    @position.setter
    def position(self, value):
        """set a position for the square"""
        if type(value) is not tuple or len(value) != 2 or\
           type(value[0]) is not int or value[0] < 0 or\
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def __str__(self):
        """print a sqaure"""

        s = ""
        if self.__size == 0:
            return s

        else:
            for i in range(self.__position[1]):
                s += "\n"

            for i in range(self.__size):
                for j in range(self.__size + self.__position[0]):
                    if j < self.__position[0]:
                        s += " "
                    else:
                        s += "#"
                if i < self.__size - 1:
                    s += "\n"

        return s
