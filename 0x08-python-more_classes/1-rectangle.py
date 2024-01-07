#!/usr/bin/python3
"""
the rectangular class
"""


class Rectangle:
    """ adding some attributes"""
    def __init__(self, width=0, height=0):
        """initiation of object"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width getting property"""
        return self.width

    @property
    def height(self):
        """Height getting property""" 
        return self.height

    @width.setter
    def width(self, value):
        """setting width with conditions"""
        if value < 0:
            raise ValueError("width must be >= 0")
        if type(value) is not int:
            raise TypeError("width must be an integer")
        self.width = value

    @height.setter
    def height(self, value):
        """setting height with conditions"""
        if value < 0:
            raise ValueError("height must be >= 0")
        if type(value) is not int:
            raise TypeError("height must be an integer")
        self.height = value
