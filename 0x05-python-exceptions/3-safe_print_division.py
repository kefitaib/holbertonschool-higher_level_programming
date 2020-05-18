#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        x = a / b
        return x

    except ZeroDivisionError:
        b = False

    else:
        b = True

    finally:
        print("Inside result: ", end="")
        if not b:
            print("None")
        else:
            print("{}".format(a / b))
