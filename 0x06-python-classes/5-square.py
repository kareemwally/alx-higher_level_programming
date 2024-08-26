#!/usr/bin/python3
"""
adding some attributes and features to the class
"""


class Square:
    """adding size instance attribute"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """
        the getter method of size property
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setting the property size with some precautions
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        the area of square is size^2
        """
        return self.__size ** 2

    def my_print(self):
        """
        printing the shape of square with # char
        """
        if self.size:
            shape = '#'*self.size
            for i in range(self.size):
                print(shape)
        else:
            print()
