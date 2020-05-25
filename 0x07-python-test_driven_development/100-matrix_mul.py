#!/usr/bin/python3
"""

Module - matrix mul

"""


def matrix_mul(m_a, m_b):
    """
    multiplies 2 matrices
    """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")

    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if any(not isinstance(x, list) for x in m_a):
        raise TypeError("m_a must be a list of lists")

    if any(not isinstance(x, list) for x in m_b):
        raise TypeError("m_b must be a list of lists")

    if not m_a or any(not x for x in m_a):
        raise ValueError("m_a can't be empty")

    if not m_b or any(not x for x in m_b):
        raise ValueError("m_b can't be empty")

    if any(not isinstance(y, (int, float)) for x in m_a for y in x):
        raise TypeError("m_a should contain only integers or floats")

    if any(not isinstance(y, (int, float)) for x in m_b for y in x):
        raise TypeError("m_b should contain only integers or floats")

    if any(len(m_a[0]) != len(x) for x in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if any(len(m_b[0]) != len(x) for x in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    res = [[0 for j in range(len(m_b[0]))] for i in range(len(m_a))]
    for k in range(len(m_a)):
        for i in range(len(m_a[0])):
            for j in range(len(m_b[0])):
                res[k][j] += m_a[k][i] * m_b[i][j]

    return res
