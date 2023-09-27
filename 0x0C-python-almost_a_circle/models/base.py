#!/usr/bin/python3
"""A Base Class"""


class Base:
    """The Base Class created
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Init method

        Args:
            id (int): _description_. number of objects created.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
