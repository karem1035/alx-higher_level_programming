#!/usr/bin/python3
"""
    A geometery class
"""


class BaseGeometry:

    """area method"""
    def area(self):

        """raising exception if not implemented"""
        raise Exception("area() is not implemented")
    

    """Method validate int"""
    def integer_validator(self, name, value):
        if type(value) != "int":
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))