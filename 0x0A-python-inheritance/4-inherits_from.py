#!/usr/bin/python3
"""Module to check if the object is an instance of a class """


def inherits_from(obj, a_class):
    """Function that checks if  the object is an instance of a subclass
    :param obj: object to check
    :param a_class: class to check
    :return: True if obj is from subclass of a_class, else, False
    """
    obj_class = type(obj)
    while obj_class != object:
        if obj_class == a_class:
            return True
        else:
            obj_class = obj_class.__base__
    return False
