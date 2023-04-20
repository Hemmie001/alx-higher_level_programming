#!/usr/bin/python3
"""Class Square Module"""

from .rectangle import Rectangle
import json


class Square(Rectangle):
    """Class Square"""
    def __init__(my_suare, size, x=0, y=0, id=None):
        """Class constructor - method"""
        super().__init__(size, size, x, y, id)
        my_suare.size = size

    def __str__(my_suare):
        """__str__ method for Square"""
        return "[Square] ({}) {}/{} - {}".format(
            my_suare.id, my_suare.x, my_suare.y, my_suare.width)

    @property
    def size(my_suare):
        """size getter"""
        return my_suare.width

    @size.setter
    def size(my_suare, value):
        """Width setter"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be > 0')
        my_suare.width = value
        my_suare.height = value

        def update(my_suare, *args, **kwargs):
            """updates values of my_quare instance from args or kwargs"""
            attributes = ["id", "size", "x", "y"]
            if args is not None:
                for i in range(len(args)):
                    setattr(my_suare, attributes[i], args[i])
            if len(args) == 0 or args[0] == "":
                if kwargs is not None:
                    for key, value in kwargs.items():
                        setattr(my_suare, key, value)

        def to_dictionary(my_suare):
            """returns the dictionary representation of the Square instance"""
            return {
                    'id': my_suare.id,
                    'size': my_suare.size,
                    'x': my_suare.x,
                    'y': my_suare.y
                   }
