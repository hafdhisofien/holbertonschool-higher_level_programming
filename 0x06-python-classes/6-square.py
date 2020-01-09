#!/usr/bin/python3
class Square:
    """" A simple Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Example function with PEP 484 type annotations.
        Args:
        self: self.
        size: size of my_square.
        postion: position of my_square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter of size.
        Args:
        slef: self.
        Returns: size of my_square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter of my size.
        Args:
        self: self.
        value: value of my size.
        Returns:none.
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Get position.
        Args:
        self:self.
        Returns:
        None.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ set postion
        Args
        self:self.
        value:position .
        Returns:
        None.
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if type(x) is not int or type(y) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ area of my_square.
        Args:
        self: self.
        Returns:
        returns the area of my_square.
        """
        area = self.__size * self.__size
        return(area)

    def my_print(self):
        """ prints a sqaure
        Args:
        self:self
        Return:
        None.
        """
        if self.size == 0:
            print('')
            return
        x, y = self.__position
        for i in range(x):
            print('')
        for i in range(self.__size):
            print("{}{}".format(' ' * y, '#' * self.__size))
