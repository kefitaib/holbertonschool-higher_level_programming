#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)

    except:
        print("Exception: {0}".format(sys.exc_info()[1]), file=sys.stderr)
