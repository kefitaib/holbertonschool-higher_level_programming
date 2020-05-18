#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        x = a / b
        return x

    except ZeroDivisionError:
        x = 0

    finally:
        print("Inside result: ", end="")
        if x == 0:
            print("None")
        else:
            print("{}".format(x))
