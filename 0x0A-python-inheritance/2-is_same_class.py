#!/usr/bin/python3
"""Module to check if object is an instance of class"""


def is_same_class(obj, a_class):
    """Function that check if object is an instance of specified class
    :param obj: object
    :param a_class: class
    :return: True if obj is from class else, False
    """
    if type(obj) == a_class:
        return True
    else:
        return False
