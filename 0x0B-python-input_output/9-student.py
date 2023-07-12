#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """Student class definition"""

    def __init__(self, first_name, last_name, age):
        """Constructor initializater"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method to retrieves a dictionary representation"""
        return (self.__dict__)
