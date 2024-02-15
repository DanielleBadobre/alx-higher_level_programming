#!/usr/bin/python3
"""Module to check if object is an instance of class"""


def is_kind_of_class(obj, a_class):
    """Function that check if object is an instance of specified class
    :param obj: object
    :param a_class: class
    :return: True if obj is from class else, False
    """
    return isinstance(obj, a_class)
