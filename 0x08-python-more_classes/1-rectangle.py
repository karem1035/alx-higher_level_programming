#!/usr/bin/python3
"""A simple rectangle class"""


class Rectangle:
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    """Return the height"""
    @property
    def height(self):
        return self.__height
    
    """sett the height"""
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    """Return the width"""
    @property
    def width(self):
        return self.__width
    
    """width setter"""
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
