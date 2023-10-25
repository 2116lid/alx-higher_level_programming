#!/usr/bin/python3
""" A square class """


class Square:
    """ Square class with attribute """

    def __init__(self, size=0):
        """ using the init method.

        Args:
           size (int): a private attribute.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ A function to return area of square. """
        return (self.__size ** 2)
