#!/usr/bin/python3
""" Definition of a class. """


class Square:
    """ a square class """

    def __init__(self, size=0, position=(0, 0)):
        """using init to initialize size position.

        Args:
           size (int): attribute of square class.
           position(int, int): attribute of class square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """gets current size of square """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """gets current position of square """
        return (self.__position)

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2\
                and all(isinstance(num, int) for num in value)\
                and all(num >= 0 for num in value):
            self.__position = value
        else:
            print("position must be a tuple of 2 positive integers")

    def area(self):
        """returns area of square """
        return (self.__size ** 2)

    def my_print(self):
        """prints # character on stdout """
        if self.__size == 0:
            print("")
        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for l in range(self.__size)]
            print("")