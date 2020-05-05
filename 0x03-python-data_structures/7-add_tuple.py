#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    t = [0, 0]
    for i in range(2):
        if i < len(tuple_a):
            t[i] += tuple_a[i]
        if i < len(tuple_b):
            t[i] += tuple_b[i]

    tup = t[0], t[1]
    del t
    return tup
