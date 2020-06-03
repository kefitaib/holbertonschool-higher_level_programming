#!/usr/bin/python3
"""
Module
"""


def pascal_triangle(n):
    """ function """

    l = []
    if n <= 0:
        return l

    for x in range(n):
        if x == 0:
            l.append([1])

        else:
            l2 = [1]
            if len(l) == 1:
                l2.append(1)
                l.append(l2)

            else:
                for i in range(x - 1):
                    l2.append(l[x - 1][i] + l[x - 1][i + 1])

                l2.append(1)
                l.append(l2)

    return l
