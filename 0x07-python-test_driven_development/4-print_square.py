#!/usr/bin/python3
"""Module to print a square"""


def print_square(size):
    """
    Function to print a square with the # symbol
    :param size: length size of the square
    :return: nothing
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            if j == (size - 1):
                print("#", end="\n")
            else:
                print("#", end="")
