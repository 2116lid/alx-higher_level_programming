#!/usr/bin/python3
"""
   This module is 0-add_integer
   it supplies one function, add_integer(a, b)

"""


def add_integer(a, b=98):
    """ Returns sum of two number
    If Float num is provided it will be typecasted before adding.
    Raises:
         TypeError: If either of the arguments are not numbers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
