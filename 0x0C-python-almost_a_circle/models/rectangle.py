#!/usr/bin/python3
"""
Module - class
"""


from models.base import Base


class Rectangle(Base):
    """ class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        if not isinstance(val, int):
            raise TypeError("width must be an integer")

        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        if not isinstance(val, int):
            raise TypeError("height must be an integer")

        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if not isinstance(val, int):
            raise TypeError("x must be an integer")

        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        if not isinstance(val, int):
            raise TypeError("y must be an integer")

        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """ return the area of the rectangle """

        return self.__width * self.__height

    def display(self):
        """ print Rectangle instance with the character # """

        for i in range(self.__y):
            print()

        for i in range(self.__height):
            for j in range(self.__width + self.__x):
                if j < self.__x:
                    print(" ", end="")
                else:
                    print("#", end="")
            print()

    def __str__(self):
        return "[Rectangle] (" + str(self.id) + ") " + str(self.__x) +\
            "/" + str(self.__y) + " - " + str(self.__width) + "/" +\
            str(self.__height)

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """

        if args is not None and len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.__width = args[i]
                if i == 2:
                    self.__height = args[i]
                if i == 3:
                    self.__x = args[i]
                if i == 4:
                    self.__y = args[i]

        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                if k == "width":
                    self.__width = v
                if k == "height":
                    self.__height = v
                if k == "x":
                    self.__x = v
                if k == "y":
                    self.__y = v

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """

        return {'id': self.id, 'width': self.__width, 'height': self.__height,
                'x': self.__x, 'y': self.__y}
