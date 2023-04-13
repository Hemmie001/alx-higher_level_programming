#!/usr/bin/python3
"""Student to JSON with filter"""


class Student:
    """student representation"""
    def __init__(self, first_name, last_name, age):
        """instantiates the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student
        """
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            new_dict = {}
            for element in attrs:
                if element in self.__dict__:
                    new_dict[element] = self.__dict__[element]
            return (new_dict)
        return (self.__dict__)
