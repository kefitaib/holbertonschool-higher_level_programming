#!/usr/bin/python3
def findPeakUtil(arr, low, high, n):
    """ that returns index of a peak element """

    mid = low + (high - low)/2
    mid = int(mid)

    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
        (mid == n - 1 or arr[mid + 1] <= arr[mid])):
        return arr[mid]

    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return findPeakUtil(arr, low, (mid - 1), n)

    else:
        return findPeakUtil(arr, (mid + 1), high, n)

def findPeak(arr, n):
    """ function findPeakUtil() """

    return findPeakUtil(arr, 0, n - 1, n)

def find_peak(list_of_integers):
    """ find the peak """

    if len(list_of_integers) == 0:
        return None

    return findPeak(list_of_integers, len(list_of_integers))
