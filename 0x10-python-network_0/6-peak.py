#!/usr/bin/python3
def find_peak(list_of_integers):
    """ find peak"""

    if not list_of_integers:
        return None

    lo = 0
    hi = len(list_of_integers) - 1

    while lo <= hi:
        if lo == hi:
            return list_of_integers[lo]

        mid = lo + (hi - lo) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            lo = mid + 1

        else:
            hi = mid

    return None
