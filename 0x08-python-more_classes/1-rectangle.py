#!/usr/bin/python3
class Rectangle:
    """A simple Rectangle
    """
    def __init__(self, width=0, height=0):
        """init the rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter/setter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter/setter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
