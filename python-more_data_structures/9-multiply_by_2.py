#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    sec_dictionary = {}
    for key in a_dictionary:
        sec_dictionary[key] = a_dictionary[key] * 2
    return sec_dictionary
