#!/usr/bin/python3
"""Class square."""


class Square:
    """ class square """

    def __init__(self, size=0, position=(0, 0)):
        """Args:
            size (int): square's size
        """
        self.size = size
        self.position = position

    @property
    def position(self):
        """position: position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        if value[0] < 0 or value[1] < 0 or len(value) != 2 or not all(isinstance(x, int) for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
