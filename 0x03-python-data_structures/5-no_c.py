#!/usr/bin/python3
def no_c(my_string):
    s = ""
    for i in range(len(my_string)):
        if my_string[i] not in 'cC':
            s += my_string[i]

    return s
