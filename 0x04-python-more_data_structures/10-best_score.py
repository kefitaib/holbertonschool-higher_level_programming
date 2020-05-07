#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        return max([v, k] for k, v in list(a_dictionary.items()))[1]
