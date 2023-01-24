#!/usr/bin/python3
"""
    module 2-square
    defines class square
    """


class Square:
    """
    class square definition
    Args:
        size: size of the square
    """

    def __init__(self, size=0):
        """
        initialize square
        Attributes:
            size (int): size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
