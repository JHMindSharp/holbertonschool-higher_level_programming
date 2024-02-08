#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides each element of a matrix by a divisor, rounding to 2
    decimal places.

    Parameters:
    - matrix: list of lists of integers/floats, with each row of the same size.
    - div: non-zero integer/float used as the divisor.

    Raises:
    - TypeError: If matrix isn't a list of lists of integers/floats,
    if rows vary
                 in size, or if div isn't an int/float.
    - ZeroDivisionError: If div is zero.

    Returns:
    - A new matrix with each element divided by div,
    rounded to 2 decimal places.
    """
    if not matrix:
        return []
    if not all(isinstance(row, list) for row in matrix) or not matrix:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return new_matrix
