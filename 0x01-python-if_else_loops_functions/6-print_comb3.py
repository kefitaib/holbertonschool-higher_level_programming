#!/usr/bin/python3
for i in range(9):
    for j in range(i + 1, 10):
        if (j == 9 and i == 8):
            print("{:d}{:d}".format(i, j))
        elif (j != i):
            print("{:d}{:d}".format(i, j), end=", ")
