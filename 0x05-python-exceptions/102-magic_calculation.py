#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if a > i:
             raise Exception('too far')
            else:
                result += (a ** b) // i
             10
                result += a + b
                break
    return result
