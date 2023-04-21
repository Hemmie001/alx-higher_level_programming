#!/usr/bin/python3
"""Module Base"""
import json
import csv


class Base:
    """
    Represent the base model.
    Represents the "base" for all other classes in project 0x0C*.
    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base.
        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON serialization of a list of dicts.
        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None:
            return json.dumps([])
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        if list_objs is None:
            list_obj = []
        else:
            list_obj = [var.to_dictionary() for var in list_objs]
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as file:
            file.write(Base.to_json_string(list_obj))

    @staticmethod
    def from_json_string(json_string):
        """
        Return the deserialization of a JSON string.
        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes.
        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Return a list of classes instantiated from a file of JSON strings.
        Reads from `<cls.__name__>.json`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        try:
            with open(cls.__name__ + ".json", mode="r", encoding="utf-8") as f:
                if f is None:
                    return []
                else:
                    tmp = Base.from_json_string(f.read())
                    result = []
                    for i in tmp:
                        result.append(cls.create(**i))
                    return result
        except CanNotWriteToFile:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Write the CSV serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        if list_objs is None:
            list_obj = []
        else:
            list_obj = [var.to_dictionary() for var in list_objs]
        with open(cls.__name__ + ".csv", "w", encoding="utf-8") as file:
            file.write(Base.to_json_string(list_obj))

    @classmethod
    def load_from_file_csv(cls):
        """
        Load the CSV serialization of a list of objects from a file.
        Args:
        """
        try:
            with open(cls.__name__ + ".csv", mode="r", encoding="utf-8") as f:
                if f is None:
                    return []
                else:
                    tmp = Base.from_json_string(f.read())
                    result = []
                    for i in tmp:
                        result.append(cls.create(**i))
                    return result
        except CanNotLoadFile:
            return []
