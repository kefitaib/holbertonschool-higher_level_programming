#!/usr/bin/python3
def weight_average(my_list=[]):
    return sum(list(x*y for x, y in my_list))/sum(list(y for x, y in my_list))
