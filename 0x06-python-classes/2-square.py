#!/usr/bin/python3
class Square:
    """" A simple Square"""

    def __init__(self, size=0):
        """init: Instantiation.
        Args:
        self: this square.
        size: size of my_sqaure.
        Returns:
        None.
        """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
