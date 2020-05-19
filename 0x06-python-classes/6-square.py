#!/usr/bin/python3
""" empty class Square that defines a square
"""


class Square:
    """ class that define a Square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data."""
        self.__size = size
        self.__position = position

    def area(self):
        """ retune the area of the sqaure
        """
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = size

    def my_print(self):
        if self.__size == 0:
            print()

        else:
            x = 1
            if self.__position[1] <= 0:
                x = self.__position[0]

            for i in range(self.__size):
                for j in range(self.__size + x):
                    if j < x:
                        print(" ", end="")
                    else:
                        print("#", end="")
                print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is tuple:
            if len(value) == 2:
                self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
