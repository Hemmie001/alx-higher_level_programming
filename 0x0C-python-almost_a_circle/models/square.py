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
            """updates values of the Square instance from args or kwargs"""
            if args is not None and len(args) > 0:
                i = 0
                for arg in args:
                    if i == 0:
                        my_suare.id = arg
                    elif i == 1:
                        my_suare.size = arg
                    elif i == 2:
                        my_suare.x = arg
                    elif i == 3:
                        my_suare.y = arg
                    i += 1
            elif kwargs is not None:
                for (key, value) in kwargs.items():
                    if key == "id":
                        my_suare.id = value
                    elif key == "size":
                        my_suare.size = value
                    elif key == "x":
                        my_suare.x = value
                    elif key == "y":
                        my_suare.y = value

        def to_dictionary(my_suare):
        """To dictionary method"""
        attributes = ["id", "size", "x", "y"]
        values = [my_suare.id, my_suare.width, my_suare.x, my_suare.y]
        return dict(zip(attributes, values))
