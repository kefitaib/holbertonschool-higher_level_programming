#!/usr/bin/python3
def roman_to_int(roman_string):
    res = 0
    if roman_string:
        num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        new = [v for x in roman_string for k, v in num.items() if x == k]
        new.reverse()
        print(new)
        for i in range(len(new)):
            if i <= len(new) - 2 and new[i] > new[i + 1]:
                res += new[i] - (new[i + 1] * 2)
                i += 1
            else:
                res += new[i]
    return res
