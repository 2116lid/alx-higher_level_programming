#!/usr/bin/python3
""" Definition of a class """


class MyList(list):
    """ A class that inherits from list class """

    def __init__(self):
        """ initializes the object """
        super().__init__()

    def print_sorted(self):
        """ prints a sorted list """
        print(sorted(self))
