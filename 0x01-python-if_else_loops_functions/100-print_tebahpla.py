#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        x = i
    else:
        x = i - 32
    print("{:c}".format(x), end="")
