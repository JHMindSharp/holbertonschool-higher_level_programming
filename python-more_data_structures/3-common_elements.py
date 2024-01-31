#!/usr/bin/python3
def common_elements(set_1, set_2):
    for element in set_1:
        for element in set_2:
            if element == element in set_1:
                c_set = element
    return c_set
