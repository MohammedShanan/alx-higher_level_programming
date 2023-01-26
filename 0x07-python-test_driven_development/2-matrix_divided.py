#!/usr/bin/python3
"""
Module 2-matrix_divided
Contains method that divides all elements of a matrix and returns new matrix
Requires same size lists of ints or floats, and max two decimal places
"""


def matrix_divided(matrix, div):
    """
    Returns new matrix with dividends
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_mtrx = []
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0 or \
            len(matrix[0]) == 0:
        raise TypeError(msg)
    same_len = len(matrix[0])
    for row in matrix:
        new_row = []
        if not isinstance(row, list):
            raise TypeError(msg)
        if len(row) != same_len:
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError(msg)
            new_row.append(round(i/div, 2))
        new_mtrx.append(new_row)
    return new_mtrx
