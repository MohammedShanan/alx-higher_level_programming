#!/usr/bin/python3
"""
Module 0-add_integer
Contains one method that returns an int sum
Accepts two values, whether int or float, and casts them to int before adding
"""
def add_integer(a, b=98):
    """
    Returns a + b as int
    """
    if not isinstance(a, int) and\
            not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and\
            not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
