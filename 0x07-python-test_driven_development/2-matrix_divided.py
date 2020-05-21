#!/usr/bin/python3
def matrix_divided(m, div):
    """
    divides all elements of a matrix
    """

    if type(m) is not list:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    l = len(m[0])
    for x in m:
        if type(x) is not list:
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

        if l != len(x):
            raise TypeError("Each row of the matrix must have the same size")

        for y in x:
            if type(y) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(a / div, 2) for a in y] for y in m]
