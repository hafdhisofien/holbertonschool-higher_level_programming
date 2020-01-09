#!/usr/bin/python3
class Square:
    """" A simple Square"""

    def __init__(self, size=0):
        """Example function with PEP 484 type annotations.
        Args:
        self: self.
        size: size of my_square.
        """
        self.__size = size

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
        if(value < 0):
            raise(ValueError)
        except TypeError:
            raise Exception('size must be an integer')
        except ValueError:
            raise Exception('size must be >= 0')

    def area(self):
        """ area of my_square.
        Args:
        self: self.
        Returns:
        returns the area of my_square.
        """
        area = self.__size * self.__size
        return(area)
