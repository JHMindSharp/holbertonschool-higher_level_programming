#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for element in matrix:
        row = []
        for elem in element:
            row.append(elem * elem)
        new_matrix.append(row)
    return new_matrix
