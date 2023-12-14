#!/usr/bin/python3
"""Class square."""


class Square:
    """ class square """

    def __init__(self, size=0):
        """Args:
            size (int): square's size
        """

        if type(size) is not int:
            raise TypeError("size must be >= 0")
        elif size < 0:
            raise ValueError("size must be an integer")
        else:
            self.__size = size
