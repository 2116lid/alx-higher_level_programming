#!/usr/bin/python3
""" This is definition of a class """


class Rectangle:
    """ This is a rectangle class, with attribute

    Attributes:
       number of instances (int): number of instances.
       print_symbol (all): string representation symbol.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ usage of init method to initialie.

        Args:
           width (int): attribute of rectangle class.
           height (int): attribute of the class.
        """
        type(self).number_of_instances += 1
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns rectangle with greater area.

        Args:
           rect_1 (Rect 1): The first Rectangle.
           rect_2 (Rect 2): The second Rectangle.
        Raises:
           TypeError: if rect_1 or rect_2 are not instance of rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    def __str__(self):
        """ Returns printable character of rectangle """
        if self.__height == 0 or self.__width == 0:
            return ("")
        else:
            r = ""
            for i in range(self.__height):
                r += str(self.print_symbol) * self.__width
                if i != self.__height - 1:
                    r += "\n"
            return (r)

    def __repr__(self):
        """ Returns string representation of the rectangle """
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """ Deletes an instance of rectangle """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
