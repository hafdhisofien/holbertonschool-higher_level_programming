#!/usr/bin/python3
"""Square model
"""

from models.rectangle import Rectangle
"""
importing the rectangle class to inherit from it
"""


class Square(Rectangle):
    """
    class Square that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        constructor of our class
        Args:
        size: size of square
        x: position
        y: position
        id: id of square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        overriding the __str__ method so that it
        returns [Square] (<id>) <x>/<y> - <size>
        in our case, width
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, value):
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        num_of_args = len(args)
        if num_of_args:
            self.id = args[0]
            if num_of_args > 1:
                self.size = args[1]
            if num_of_args > 2:
                self.x = args[2]
            if num_of_args > 3:
                self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs.get("id")
            if "size" in kwargs:
                self.size = kwargs.get("size")
            if "x" in kwargs:
                self.x = kwargs.get("x")
            if "y" in kwargs:
                self.y = kwargs.get("y")
