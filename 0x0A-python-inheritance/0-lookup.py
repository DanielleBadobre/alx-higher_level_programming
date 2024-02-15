#!/usr/bin/python3
"""Module that prints the list of attributes"""


def lookup(obj):
    """ function that returns the list of available attributes of an object
    :param obj: object to check
    :return: list of atributes
    """
    return dir(obj)
