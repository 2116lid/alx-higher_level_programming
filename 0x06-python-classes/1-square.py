#!/usr/bin/python3
""" definition of square class with attribut"""


class Square:
    """ A square class """

    def __init__(self, size):
        """ usage of init to initialize

        Args:
           size (int): an attribute of square.
        """
        self.__size = size
