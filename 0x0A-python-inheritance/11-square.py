#ython3
Rectangle = __import__('9-rectangle').Rectangle

"""
import my class Rectangle
"""


class Square(Rectangle):

    """
    class Square that inherits from Rectangle
    """

    def __init__(self, size):
        """
        private attributes. No getter or setter
        """
        self.__size = size
        """
        positive integers, validated by integer_validator
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """
        implemented the area method
        """
        return self.__size**2

    def __str__(self):
        """
        function that returns, the following
        rectangle description: [Square] <width>/<height>
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))
