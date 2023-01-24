#!/usr/bin/python3
"""
Module 6-square
Defines class Square with private size and public area
Can access and update size
"""


class Square:
    """
    class Square definition

    Args:
        size (int): size of a side in square

    Functions:
        __init__(self, size)
        size(self)
        size(self, value)
        area(self)
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes square

        Attributes:
            size (int): size of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """"
        Getter

        Return: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter

        Args:
            value: value of size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """"
        Getter

        Return: position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter

        Args:
            value: sets position to tuple if value is tuple of 2 positive ints
        """
        if type(value) is not tuple or len(value) < 2 or\
                type(value[0]) is not int or type(value[0]) is not int\
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates area of square
        Returns:
            area
        """
        return (self.__size)**2

    def my_print(self):
        """
        print the  square with #
        """
        if self.__size != 0:
            print("\n" * self.position[1], end="")
            print("\n".join([self.__position[0] * " "
                             + "#" * self.__size
                            for _ in range(self.__size)]))
        else:
            print()
