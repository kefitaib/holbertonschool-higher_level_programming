#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = str[:n] + str[n + 1:len(str)]
    return str2
