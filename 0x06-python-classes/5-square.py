#!/usr/bin/python3
"""Class square."""


class Square:
    """ class square """

    def __init__(self, size=0):
        """Args:
            size (int): square's size
        """
        self.size = size

    @property
    def size(self):
        """size: size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise ValueError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ returns area of square"""
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for i in range(self.__size):
                    print("#", end="")
                print("")
