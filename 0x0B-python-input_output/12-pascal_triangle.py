#!/usr/bin/python3
"""
Module 12-pascal_triangle

Contains function that returns int lists of pascal triangle of any given size
"""


def pascal_triangle(n):
    """
    Return:
        empty list [] if n <= 0
        if n is 5, we should expect:
            [1]
            [1, 1]
            [1, 2, 1]
            [1, 3, 3, 1]
            [1, 4, 6, 4, 1]
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangle = [[1]]
    for _ in range(n - 1):
        triangle += [a+b for a, b
                     in zip([0] + triangle[-1], triangle[-1] + [0])]
    return triangle
