#!/usr/bin/python3
"""importing a class from the parent"""
Rectangle = __import__("9-rectangle").Rectangle


"""A Square class that inherits from a Rectangle class"""


class Square(Rectangle):
    """A init function with the size"""

    def __init__(self, size):
        self.integer_validator("size", size)

        super().__init__(size, size)
        self.__size = size
