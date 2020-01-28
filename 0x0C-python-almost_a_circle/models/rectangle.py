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
