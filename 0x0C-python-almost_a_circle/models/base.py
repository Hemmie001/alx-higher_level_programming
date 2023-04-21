#!/usr/bin/python3
"""Module Base"""
import json
import csv


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Init function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Pass list to JSON string"""
        if list_dictionaries is None:
            return json.dumps([])
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write json to a file"""
        if list_objs is None:
            list_obj = []
        else:
            list_obj = [var.to_dictionary() for var in list_objs]
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as file:
            file.write(Base.to_json_string(list_obj))

    @staticmethod
    def from_json_string(json_string):
        """From json string"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create method"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load from a file"""
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
        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write json to a file"""
        if list_objs is None:
            list_obj = []
        else:
            list_obj = [var.to_dictionary() for var in list_objs]
        with open(cls.__name__ + ".csv", "w", encoding="utf-8") as file:
            file.write(Base.to_json_string(list_obj))

    @classmethod
    def load_from_file_csv(cls):
        """Load from a file"""
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
        except:
            return []
