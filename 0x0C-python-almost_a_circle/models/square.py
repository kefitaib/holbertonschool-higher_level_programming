#!/usr/bin/python3
"""
Module - class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ class sqaure """

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(self.size, self.size, x, y, id)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, val):
        if not isinstance(val, int):
            raise TypeError("width must be an integer")

        if val <= 0:
            raise ValueError("width must be > 0")
        self.__size = val

    def __str__(self):
        return "[Square] (" + str(self.id) + ") " + str(self.x) +\
            "/" + str(self.y) + " - " + str(self.size)

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """

        if args is not None and len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.__size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]

        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                if k == "size":
                    self.__size = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v

    def to_dictionary(self):
        """ returns the dictionary representation of a Square """

        return {'id': self.id, 'size': self.__size, 'x': self.x, 'y': self.y}
