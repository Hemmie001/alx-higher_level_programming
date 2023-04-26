#!/usr/bin/python3
"""Base class"""

import json
import os
import csv
import turtle


class Base:
    """
    represents the  Base model
    represents the base for all other calsses
    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(my_base, id=None):
        """this constructor initialises a new base"""
        if id is not None:
            my_base.id = id
        else:
            Base.__nb_objects += 1
            my_base.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON serialization of a list of dicts.
        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        list_dict = []
        for i in list_objs:
            list_dict.append(i.to_dictionary())
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as jsonfile:
            jsonfile.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """returns list of the JSON string representation from json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Return a class instantied from a dictionary of attributes.
        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        new_inst = cls(1, 1)
        if new_inst is not None:
            new_inst.update(**dictionary)
        return new_inst

    @classmethod
    def load_from_file(cls):
        """load a list of instancesfrom a file"""
        try:
            with open(str(cls.__name__) + ".json", "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Reads from `<cls.__name__>.csv`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
