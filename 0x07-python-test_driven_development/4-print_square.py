#!/usr/bin/python3
"""
Module 4-print_square
Contains method that prints square with #'s
Takes in an int size
"""


def print_square(size):
    """
    print the  square with #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("", end="")
    else:
        print("\n".join(["#" * size for _ in range(size)]))
