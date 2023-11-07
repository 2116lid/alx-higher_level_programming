#!/usr/bin/python3
""" Defining a functionn """


def inherits_from(obj, a_class):
    """ checks if obj is subclass or not """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
