#!/usr/bin/python3
"""

Function that adds 2 integers

"""
def add_integer(a, b=98):
    """
    These comments are stupid
    """
    if type(a) is not float or type(a) is not int:
        raise TypeError
    if type(b) is not float or type(b) is not int:
        raise TypeError
    return int(a) + int(b)
