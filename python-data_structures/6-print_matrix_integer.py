#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for element in matrix:
        for i, elem  in enumerate(element):
            if i < len(element) -1:
                print("{:d}".format(elem), end=" ")
            else:
                print("{:d}".format(elem), end="")
        print()
