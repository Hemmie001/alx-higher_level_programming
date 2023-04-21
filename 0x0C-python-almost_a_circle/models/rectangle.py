#!/usr/bin/python3
"""Module of Rectangle class"""
from models.base import Base


class Rectangle(Base):

    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init method"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter method"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Height getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter method"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """X getter method"""
        return self.__x

    @x.setter
    def x(self, value):
        """X setter method"""
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Y getter method"""
        return self.__y

    @y.setter
    def y(self, value):
        """Y setter method"""
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """returns the Area of the rectangle instance """
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance"""
        pos_height = self.height
        pos_width = self.width
        pos_x = self.x
        pos_y = self.y

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

    def __str__(self):
        """String method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y,
            self.width, self.height)

    def update(self, *args, **kwargs):
        """Update method"""
        attributes = ["id", "width", "height", "x", "y"]
        if args is not None:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """To dictionary method"""
        attributes = ["id", "width", "height", "x", "y"]
        values = [self.id, self.width,
                  self.height, self.x, self.y]
        return dict(zip(attributes, values))
