#!/usr/bin/python3
""" This is definition of a class """


class Rectangle:
    """ This is a rectangle class. """
    def __init__(self, width=0, height=0):
        """ usage of init method to initialie.

        Args:
           width (int): attribute of rectangle class.
           height (int): attribute of the class.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Gets the width """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Gets the height """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns the area of rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of a rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height * self.__width)

    def __str__(self):
        """ Returns printable character of rectangle """
        if self.__height == 0 or self.__width == 0:
            return ("")
        else:
            r = ""
            for i in range(self.__height):
                r += "#" * self.__width
                if i != self.__height - 1:
                    r += "\n"
            return (r)
