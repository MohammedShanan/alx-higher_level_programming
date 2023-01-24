#!/usr/bin/python3
"""
    module 4-square
    defines class square
    """


class Square:
    """
    class square definition
    Args:
        size: size of the square
    Functions:
        __init__(self, size)
        size(self)
        size(self, value)
        area(self)
    """

    def __init__(self, size=0):
        """
        initialize square
        Attributes:
            size (int): size of the square
        """
        self.size = size

    @property
    def size(self):
        """
        Getter
        Returns:size        
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter
        Args:
            value (int): size value
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        calculate the area of the square
        Returns:area
        """
        return self.__size ** 2
