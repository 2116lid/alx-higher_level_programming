#!/usr/bin/python3
"""Defining a class"""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize the attribute instances

        Args:
           width (int): the width of rectangle
           height (int): the height of rectangle.
           x (int): instance of rectangle.
           y (int): instance of rectangle.
           id (int): instance of base.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the x"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the y"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints # character"""
        if self.__width == 0 or self.__height == 0:
            print("")
            return

        for i in range(self.__y):
            print("")

        for j in range(self.__height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args and len(args) != 0:
            k = 0
            for arg in args:
                if k == 0:
                    if arg is None:
                        self.__init__(self.__width, self.__height,
                                      self.__x, self.__y)
                    else:
                        self.id = arg
                elif k == 1:
                    self.__width = arg
                elif k == 2:
                    self.__height = arg
                elif k == 3:
                    self.__x = arg
                elif k == 4:
                    self.__y = arg
                k += 1
        elif kwargs and len(kwargs) != 0:
            for key, v in kwargs.items():
                if key == "id":
                    if v is None:
                        self.__init__(self.__width, self.__height,
                                      self.__x, self.__y)
                    else:
                        self.id = v
                elif key == "width":
                    self.__width = v
                elif key == "height":
                    self.__height = v
                elif key == "x":
                    self.__x = v
                elif key == "y":
                    self.__y = v

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {"id": self.id, "width": self.__width,
                "height": self.__height, "x": self.x,
                "y": self.__y}

    def __str__(self):
        """returns printable representation of rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x, self.__y,
                                                       self.__width,
                                                       self.__height)
