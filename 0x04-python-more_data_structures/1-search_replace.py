#!/usr/bin/python
def search_replace(my_list, search, replace):
    l = list(map(lambda x: x if (x != search) else replace, my_list))
    return l
