#!/usr/bin/python3
"""Base Class"""


class Base:
    """Base Class Created"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Init method

        Args:
            id: number of inits. Defaults to None.
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
