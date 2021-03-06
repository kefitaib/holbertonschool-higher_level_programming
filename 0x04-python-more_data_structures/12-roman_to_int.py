#!/usr/bin/python3
def roman_to_int(roman_string):
    res = 0
    if type(roman_string) is str and roman_string:
        num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        new = [v for x in roman_string for k, v in num.items() if x == k]
        for i in reversed(range(len(new))):
            if i >= 1 and new[i] > new[i - 1]:
                res -= new[i - 1] * 2
            res += new[i]

    return res
