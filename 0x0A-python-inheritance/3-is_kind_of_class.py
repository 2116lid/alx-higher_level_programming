#!/usr/bin/python3
""" Defining a function """


def is_kind_of_class(obj, a_class):
    """ returns true or false considering inheritance """
    if isinstance(obj, a_class):
        return True
    return False
