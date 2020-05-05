#!/usr/bin/python3
def multiple_returns(sentence):
    x = len(sentence)
    if x > 0:
        t = x, sentence[0]
    else:
        t = x, None

    return t
