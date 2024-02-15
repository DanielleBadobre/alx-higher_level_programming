#!/usr/bin/python3
"""Module to check if the object is an instance of a class """


def inherits_from(obj, a_class):
    """Function that checks if  the object is an instance of a subclass
    :param obj: object to check
    :param a_class: class to check
    :return: True if obj is from subclass of a_class, else, False
    """
    return type(obj) != a_class and isinstance(obj, a_class)
