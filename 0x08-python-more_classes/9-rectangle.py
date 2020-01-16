#!/usr/bin/python3
class Rectangle:
    """A simple Rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """init the rectangle and Incrementes the number of instances"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter/setter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of my width.
        Args:
        self: self.
        value: value of my width.
        Returns:none. """
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
        """setter of my height.
        Args:
        self: self.
        value: value of my height.
        Returns:none.
        """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return: area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return: Perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """print the rectangle with the character #.
        Args:
        self: self..
        Returns:returns my rectangle in #.
        """
        if self.width == 0 or self.height == 0:
            return ("")
        width = ("{}".format(self.print_symbol)) * self.width
        rectangle = width
        for x in range(self.height - 1):
            rectangle += "\n" + width
        return (rectangle)

    def __repr__(self):
        """Returns : string representation of the rectangle"""
        return ("Rectangle({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
        """Returns: a message when an instance is deleted and
        Decrementes the number of instances"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns: the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() < rect_2.area():
            return (rect_2)
        return (rect_1)

    @classmethod
    def square(cls, size=0):
        """Returns:a new Rectangle instance with width == height == size"""
        return (cls(size, size))
