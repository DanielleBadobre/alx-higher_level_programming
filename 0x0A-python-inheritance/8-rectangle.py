#!/usr/bin/python3
""" Module for an empty class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class to create a rectangle"""
    def __init__(self, width, height):
        """initialization"""
        self.__width = width
        self.__height = height
        self.integer_validator("height", self.__height)
        self.integer_validator("width", self.__width)
