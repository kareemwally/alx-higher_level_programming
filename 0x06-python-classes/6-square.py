#!/usr/bin/python3
"""
adding some attributes and features to the class
"""


class Square:
    """adding size instance attribute"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """property position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setting position property"""
        if type(value) is not tuple or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        the area of square is size^2
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using the '#' character and handle position."""
        if self.size == 0:
            print()
            return

        # Print position[1] empty lines (top margin)
        for _ in range(self.position[1]):
            print()

        # Print the square with spaces before the '#'
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
