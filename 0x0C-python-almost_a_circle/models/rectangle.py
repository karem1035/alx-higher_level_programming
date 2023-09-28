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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Width getter and setter
    @property
    def width(self):
        """Returnning width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setting the width of the rectangle"""

        # Type Validator
        if type(width) is not int:
            raise TypeError(f"width must be an integer")

        # Value Validator
        if width < 1:
            raise ValueError(f"width must be > 0")

        self.__width = width

    # Height getter and setter
    @property
    def height(self):
        """Returnning height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setting the height of the rectangle"""

        # Type Validator
        if type(height) is not int:
            raise TypeError(f"height must be an integer")

        # Value Validator
        if height < 1:
            raise ValueError(f"height must be > 0")

        self.__height = height

    # X getter and setter
    @property
    def x(self):
        """Returnning x of the rectangle"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setting x of the square"""

        # Type Validator
        if type(x) is not int:
            raise TypeError(f"x must be an integer")

        # Value Validator
        if x < 0:
            raise ValueError(f"x must be >= 0")

        self.__x = x

    # Y getter and setter
    @property
    def y(self):
        """Returnning y of the square"""
        return self.__y

    @y.setter
    def y(self, y):
        """setting y of the squrare"""

        # Type Validator
        if type(y) is not int:
            raise TypeError(f"y must be an integer")

        # Value Validator
        if y < 0:
            raise ValueError(f"y must be >= 0")

        self.__y = y

    def area(self):
        """Return the area of the rectangle"""
        return self.height * self.width

    def display(self):
        """Display the rectangle with #s"""
        for _ in range(self.y):
            print()
        for i in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """The str of the Rectangle"""

        return f"[Rectangle] ({self.id}) {self.x}/{self.y}\
 - {self.width}/{self.height}"
