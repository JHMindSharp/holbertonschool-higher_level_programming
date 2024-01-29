#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for actual_element in matrix:
        for i in range(len(actual_element)):
            element = actual_element[i]
            actual_element[i] = element
    for actual_element in matrix:
        print(" ".join(map(str, actual_element)))
