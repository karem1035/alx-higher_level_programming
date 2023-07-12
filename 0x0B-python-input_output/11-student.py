#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """Student class definition"""

    def __init__(self, first_name, last_name, age):
        """Constructor initializater"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method to retrieves a dictionary representation
        if attrs is a list of strings, only attribute names contained
        in this lists must be retrieved, otherwise, all attributes
        must be retrieved"""

        result = {}

        if attrs is None:
            return (self.__dict__)

        for key in attrs:
            """If not find key in the class return None, for that
            this class should be transform in dictionary"""
            value = self.__dict__.get(key)
            if value is not None:
                result[key] = value
        return (result)

    def reload_from_json(self, json):
        """Method that replaces all attributes of the student instance"""

        dict_new = self.__dict__

        for key, value in json.items():
            if (dict_new.get(key) == self.first_name):
                self.first_name = value
            elif (dict_new.get(key) == self.last_name):
                self.last_name = value
            elif (dict_new.get(key) == self.age):
                self.age = value
