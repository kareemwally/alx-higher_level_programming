#!/usr/bin/python3
"""
the rectangular class
"""



class Rectangle:
    """ adding some attributes"""
    def __init__(self, width=0, height=0):
        self.width(self, width)
        self.height(self, height)

    @property
    def width(self):
        return self.__width
    @property
    def height(self):
        return self.__height
    @width.setter
    def width(self, value):
        self.__width = value
        assert value >= 0, "width must be >= 0"
        assert type(value) == type(100), "width must be an integer"
    @height.setter
    def height(self, value):
        self.__height = value
        assert value >= 0, "height must be >= 0"
        assert type(value) == type(100), "height must be an integer"
