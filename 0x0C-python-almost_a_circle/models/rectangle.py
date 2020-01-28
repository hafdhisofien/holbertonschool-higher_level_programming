#!/usr/bin/python3
"""Rectangle model
"""

from models.base import Base
"""
importing the bas class to inherit from it
"""


class Rectangle(Base):
    """
    class Rectangle that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        constructor of our class
        Args:
        width
        height
        x: position
        y: position
        id: id of rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        returns the area value of the Rectangle instance
        """
        return self.__width * self.__height

    def display(self):
        """
        prints in stdout the Rectangle instance with the character #
        """
        for i in range(self.y):
            print()
        for j in range(self.__height):
            print("{}".format(self.x * " "), end='')
            print("{}".format(self.width * '#'))

    def __str__(self):
        """
        overriding the __str__ method so that it
        returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """

        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id,
                                                self.__x, self.__y,
                                                self.__width,
                                                self.__height)

    def update(self, *args):
        """
        assigns an argument to each attribute
        """
        num_of_args = len(args)
        if num_of_args:
            self.id = args[0]
            if num_of_args > 1:
                self.width = args[1]
            if num_of_args > 2:
                self.height = args[2]
            if num_of_args > 3:
                self.x = args[3]
            if num_of_args > 4:
                self.y = args[4]
