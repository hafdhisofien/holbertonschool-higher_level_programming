#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        """Example function with PEP 484 type annotations.
        Args:
        slef: The first parameter.
        size: The size of my_square.
        """
        self.__size = size
        try:
            size += 1
            if(size < 0):
                raise(ValueError)
        except TypeError:
            raise Exception('size must be an integer')
        except ValueError:
            raise Exception('size must be >= 0')

    def area(self):
        """Example function with PEP 484 type annotations.
        Args:
        param1: The first parameter.
        param2: The second parameter.
        Returns:
        returns the area of my_square.
        """
        area = self.__size * self.__size
        return(area)
