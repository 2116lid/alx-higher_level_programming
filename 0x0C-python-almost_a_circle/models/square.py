#!/usr/bin/python3
"""Defining a class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the instances

        Args:
           size (int): The size of the Square.
           x (int): The x coordinate.
           y (int): The y coordinate.
           id (int): The identity of the Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """gets the size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes and updates the class"""
        if args and len(args) != 0:
            k = 0
            for arg in args:
                if k == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif k == 1:
                    self.size = arg
                elif k == 2:
                    self.x = arg
                elif k == 3:
                    self.y = arg
                k += 1

        elif kwargs and len(kwargs) != 0:
            for key, v in kwargs.items():
                if key == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif key == "size":
                    self.size = v
                elif key == "x":
                    self.x = v
                elif key == "y":
                    self.y = v

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}

    def __str__(self):
        """Returns printable representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
