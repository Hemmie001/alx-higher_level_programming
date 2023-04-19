#!/usr/bin/python3
"""Module of Rectangle class"""
from models.base import Base


class Rectangle(Base):

    """Class Rectangle"""

    def __init__(my_rectangle, width, height, x=0, y=0, id=None):
        """Init method"""
        my_rectangle.width = width
        my_rectangle.height = height
        my_rectangle.x = x
        my_rectangle.y = y
        super().__init__(id)

    @property
    def width(my_rectangle):
        """Width getter method"""
        return my_rectangle.__width

    @width.setter
    def width(my_rectangle, value):
        """Width setter method"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        my_rectangle.__width = value

    @property
    def height(my_rectangle):
        """Height getter method"""
        return my_rectangle.__height

    @height.setter
    def height(my_rectangle, value):
        """Height setter method"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        my_rectangle.__height = value

    @property
    def x(my_rectangle):
        """X getter method"""
        return my_rectangle.__x

    @x.setter
    def x(my_rectangle, value):
        """X setter method"""
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        my_rectangle.__x = value

    @property
    def y(my_rectangle):
        """Y getter method"""
        return my_rectangle.__y

    @y.setter
    def y(my_rectangle, value):
        """Y setter method"""
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        my_rectangle.__y = value

    def area(my_rectangle):
        """returns the Area of the rectangle instance """
        return my_rectangle.__width * my_rectangle.__height

    def display(my_rectangle):
        """prints in stdout the Rectangle instance"""
        pos_height = my_rectangle.height
        pos_width = my_rectangle.width
        pos_x = my_rectangle.x
        pos_y = my_rectangle.y

        if pos_height == 0 or pos_width == 0:
            print()
            return

        for k in range(pos_y):
            print()

        for i in range(pos_height):
            print(' ' * pos_x, end='')
            for j in range(pos_width):
                print('#', end='')
            print()

    def __str__(my_rectangle):
        """String method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            my_rectangle.id, my_rectangle.x, my_rectangle.y, my_rectangle.width, my_rectangle.height)

    def update(my_rectangle, *args, **kwargs):
        """Update method"""
        attributes = ["id", "width", "height", "x", "y"]
        if args is not None:
            for i in range(len(args)):
                setattr(my_rectangle, attributes[i], args[i])
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(my_rectangle, key, value)

    def to_dictionary(my_rectangle):
        """To dictionary method"""
        attributes = ["id", "width", "height", "x", "y"]
        values = [my_rectangle.id, my_rectangle.width, my_rectangle.height, my_rectangle.x, my_rectangle.y]
        return dict(zip(attributes, values))
