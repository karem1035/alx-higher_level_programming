#!/usr/bin/python3

"""Importing base gemotry"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


"""
    A Rectangle class that inherits from BaseGeometry
"""


class Rectangle(BaseGeometry):

    """instance definition"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    """Are of the rectangle method"""

    def area(self):
        return self.__width * self.__height

    """Base str method"""

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
