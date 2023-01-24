#!/usr/bin/python3
"""Define MagicClass"""
import math


class MagicClass:
    """Initialize and define methods area and circumference"""
    def __init__(self, radius):
        """Initialize MagicClass"""
        self.__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculate area"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculate circumference"""
        return 2 * math.pi * self.__radius
