#!/usr/bin/python3
import math
import dis
"""magig class"""


class MagicClass:
    """calculate area and circumference"""

    def __init__(self, radius=0):
        self.___radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.___radius = radius

    def area(self):
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
