#!/usr/bin/python3
def print_square(size):
    """
    prints a square with the character #
    """

    if type(size) not in [int, float]:
        raise TypeError("size must be an integer")

    if size < 0 and type(size) is float:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if type(size) is float:
        size = int(size)

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
