#!/usr/bin/python3

"""Importing base gemotry"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


"""
    A Rectangle class that inherits from BaseGeometry
"""


class Rectangle(BaseGeometry):

    """inst definition"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
