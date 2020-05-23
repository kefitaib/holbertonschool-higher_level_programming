#!/usr/bin/python3
"""

Module - text_indentation

"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    s2 = text[::-1]
    for i in range(len(s2)):
        if s2[i] != ' ':
            s = s2[i:]
            break

    text = s[::-1]

    s = ""
    x = 0
    for i in text:
        if i != ' ':
            x = 1

        if x == 1:
            s += i

        if i in ".:?":
            print(s)
            print()
            s = ""
            x = 0
    print(s)
    print()
