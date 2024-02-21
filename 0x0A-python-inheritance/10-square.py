#!/usr/bin/python3
""" Module for an empty class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class to create a square"""
    def __init__(self, size):
        """ initialize"""
        self.__size = size
        self.integer_validator("size", self.__size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return (f"[Rectangle] {self.__size}/{self.__size}")
