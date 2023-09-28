#!/usr/bin/python3
"""Importing the base class"""

from models.base import Base


class Rectangle(Base):
    """Rectangle

    Args:
        Base (base class): The super class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    # Width getter and setter
    @property
    def get_width(self):
        """Returnning width of the rectangle"""
        return (__width)

    @width.setter
    def width(self, width):
        """Setting the width of the rectangle"""
        self.__width = width

    # Height getter and setter
    @property
    def height(self):
        """Returnning height of the rectangle"""
        return (__height)

    @height.setter
    def height(self, height):
        """Setting the height of the rectangle"""
        self.__height = height

    # X getter and setter
    @property
    def x(self):
        """Returnning x of the rectangle"""
        return (__x)

    @x.setter
    def x(self, x):
        """Setting x of the square"""
        self.__x = x

    # Y getter and setter
    @property
    def y(self):
        """Returnning y of the square"""
        return (__y)

    @y.setter
    def y(self, y):
        """setting y of the squrare"""
        self.__y = y
