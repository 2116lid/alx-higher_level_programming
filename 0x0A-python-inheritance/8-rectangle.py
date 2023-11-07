#!/usr/bin/python3
""" Defining a rectangle class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A rectangle class """
    def __init__(self, width, height):
        """ Initializes a new Rectangle geometry """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
