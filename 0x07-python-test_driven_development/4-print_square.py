#!/usr/bin/python3
""" This module contains one function """


def print_square(size):
    """ prints "#" character with square shape

    Args:
       size (int): is the size length of the square.
    Raises:
       TypeError: If size is not an integer
       ValueError: If size is lessthan 0.
       TypeError: is a float and is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print("")
