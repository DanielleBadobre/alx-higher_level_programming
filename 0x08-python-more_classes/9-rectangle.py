#!/usr/bin/python3
"""Creating a class rectangle that defines a rectangle by width and height"""


class Rectangle:
    """Instantiation with optional width and height"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if (self.__height != 0) and (self.__width != 0):
            return 2 * (self.__height + self.__width)
        else:
            return 0

    def __str__(self):
        if (self.__height != 0) and (self.__width != 0):
            return (((self.__height - 1) * ((self.__width *
                    str(self.print_symbol)) + "\n")) + self.__width *
                    str(self.print_symbol))
        else:
            return ""

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle):
            if isinstance(rect_2, Rectangle):
                if rect_1.area() >= rect_2.area():
                    return rect_1
                else:
                    return rect_2
            else:
                raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            raise TypeError("rect_1 must be an instance of Rectangle")

    @classmethod
    def square(cls, size=0):
        return cls(width=size, height=size)
