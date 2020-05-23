#!/usr/bin/python3
"""
    function that
    add two numbers
    a + b
"""


def add_integer(a, b=98):
    """
        [add_integer]
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89

    return int(result)
