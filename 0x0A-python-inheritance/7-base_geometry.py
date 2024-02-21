#!/usr/bin/python3
""" Module for an empty class"""


class BaseGeometry:
    """ class basegeometry """
    def area(self):
        """ public instance method to raise exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Public instance method that validates value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
