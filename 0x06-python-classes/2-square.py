#!/usr/bin/python3
""" A square class """


class Square:
    """ A square class with sie attribute """

    def __init__(self, size=0):
        """ usage of init.

        Args:
            size (int): private attribute of square class.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
