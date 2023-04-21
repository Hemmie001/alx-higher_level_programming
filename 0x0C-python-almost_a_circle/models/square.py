#!/usr/bin/python3
"""contains class Square implements class Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        this Square repreesentation implements rectangle
    """
    def __init__(my_square, size, x=0, y=0, id=None):
        """
            initialises Square (overrides Rectangle init)
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(my_square):
        """returns the size of the square"""
        return my_square.width

    @size.setter
    def size(my_square, value):
        """sets the value of size"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        my_square.width = value
        my_square.height = value

    def update(my_square, *args, **kwargs):
        """
            assigns key/value argument to attributes
            kwargs is skipped if args is not empty
            Args:
                *args -  variable number of no-keyword args
                **kwargs - variable number of keyworded args
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                my_square.__setattr__(key, val)
            return

        try:
            my_square.id = args[0]
            my_square.size = args[1]
            my_square.x = args[2]
            my_square.y = args[3]
        except IndexError:
            pass

    def __str__(my_square):
        """Overloading str function"""
        return "[{}] ({}) {}/{} - {}".format(type(my_square).__name__,
                                             my_square.id, my_square.x,
                                             my_square.y,
                                             my_square.width)

    def to_dictionary(my_square):
        """
            Returns the dictionary representation of a Square
        """
        return {'id': getattr(my_square, "id"),
                'size': getattr(my_square, "width"),
                'x': getattr(my_square, "x"),
                'y': getattr(my_square, "y")}
