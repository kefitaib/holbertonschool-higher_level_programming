#!/usr/bin/python
def search_replace(my_list, search, replace):
    l = []
    for x in my_list:
        if x == search:
            y = replace
        else:
            y = x
        l.append(y)
    return l
