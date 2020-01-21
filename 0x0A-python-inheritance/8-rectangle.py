#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
import my class BaseGeometry
"""


class Rectangle(BaseGeometry):

    """
    class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        private attributes. No getter or setter
        """
        self.__width = width
        self.__height = height
        """
        positive integers, validated by integer_validator
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
