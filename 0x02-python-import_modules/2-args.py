#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len = len(sys.argv)
    if len == 1:
        print("{:d} arguments.".format(0))
    elif len == 2:
        print("{:d} argument:".format(1))
    else:
        print("{:d} arguments:".format(len - 1))

    for i in range(1, len):
        print("{:d}: {:s}".format(i, sys.argv[i]))
