#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dictionary = {'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    total = 0
    prev_value = 0

    for element in reversed(roman_string):
        value = roman_dictionary[element]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total
