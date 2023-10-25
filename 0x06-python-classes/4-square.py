#!/usr/bin/python3
""" Defining a square class """


class Square:
    """ a square class with size """

    def __init__(self, size=0):
        """ using init to initializ.

        Args:
          size (int): attribute of square class.
        """
        self.size = size

    @property
    def size(self):
        """ a function that returns private instance of size """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ a function that return area of square """
        return (self.size ** 2)
