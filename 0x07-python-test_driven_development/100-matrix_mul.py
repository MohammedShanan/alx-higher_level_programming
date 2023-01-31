#!/usr/bin/python3
"""
Module 100-matrix_mul
Contains method that does matrix multiplication
Requires same size lists/rows of ints or floats
"""


def validate_matrices(m_a, m_b):
    """
    validate matrices
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    elif not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if m_a == [[]] or m_a == []:
        raise ValueError("m_a can't be empty")
    elif m_b == [[]] or m_b == []:
        raise ValueError("m_b can't be empty")
    for eachrow in m_a:
        if not isinstance(eachrow, list):
            raise TypeError("m_a must be a list of lists")
        for n in eachrow:
            if not isinstance(n, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
        if len(eachrow) != len(m_a[0]):
            raise TypeError("each row of m_a must should be of the same size")

        for eachrow in m_b:
            if not isinstance(eachrow, list):
                raise TypeError("m_b must be a list of lists")
            for n in eachrow:
                if not isinstance(n, (int, float)):
                    raise TypeError(
                        "m_b should contain only integers or floats")
            if len(eachrow) != len(m_b[0]):
                raise TypeError(
                    "each row of m_b must should be of the same size")


def matrix_mul(m_a, m_b):
    """
    Returns resulting matrix multiplication
    """
    validate_matrices(m_a, m_b)
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    new_matrx = []
    for row_a in m_a:
        new_row = []
        for i in range(len(m_b[0])):
            n = 0
            for j in range(len(m_b)):
                n += m_b[j][i] * row_a[j]
            new_row.append(n)
        new_matrx.append(new_row)
    return new_matrx
