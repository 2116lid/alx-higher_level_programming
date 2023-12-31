#!/usr/bin/python3
""" definition of square class. """


class Square:
    """ a square class with attribute """

    def __init__(self, size=0):
        """ using init method.

        Args:
           size (int): attribute of square class.
        """
        self.size = size

    @property
    def size(self):
        """using property to get current size """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns area of square """
        return (self.__size ** 2)

    def my_print(self):
        """prints # character in stdout """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
