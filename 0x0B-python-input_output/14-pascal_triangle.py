#!/usr/bin/python3
"""
Module
"""


def pascal_triangle(n):
    """ function """

    l = []
    if n <= 0:
        return l

    for x in range(1, n + 1):
        if x == 1:
            l.append([1])

        else:
            l2 = [1]
            if len(l) == 1:
                l2.append(1)
                l.append(l2)

            else:
                for i in range(1, x - 1):
                    l2.append(l[x - 2][i - 1] + l[x - 2][i])

                l2.append(1)
                l.append(l2)

    return l
