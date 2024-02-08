#!/usr/bin/python3


def add_integer(a, b=98):
    """
    Function to add 2 numbers
    :param a: first number
    :param b: second number
    :return: the sum of a and b
    """
    if type(a) != int:
        if type(a) == float:
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    if type(b) != int:
        if type(b) == float:
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    return a + b
