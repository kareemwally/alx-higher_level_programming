#!/usr/bin/python3
"""
the rectangle class module
"""


from models.base import Base


class Rectangle(Base):
    """the rectangle class body"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor of instances"""
        super().__inint(id)
        self.width = width
        self.h`eight = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """the width getter"""
        return self.__width

    @property
    def height(self):
        """the height getter"""
        return self.__height

    @width.setter
    def width(self, value):
        """the width setter"""
        self.__width = value

    @height.setter
    def height(self, value):
        """the height setter"""
        self.__height = value

    @property
    def x(self):
        """the x getter"""
        return self.__x

    @property
    def y(self):
        """the y getter"""
        return self.__y

    @x.setter
    def x(self, value):
        """the x setter"""
        self.__x = value

    @y.setter
    def y(self, value):
        """the y setter"""
        self.__y = value
