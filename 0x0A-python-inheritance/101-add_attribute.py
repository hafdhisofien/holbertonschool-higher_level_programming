#!/usr/bin/python3
"""
Can I? YES YOU CAN
"""


def add_attribute(self, name, value):
    """
    function that adds a new attribute to an object if it’s possible
    """

    you_cant = {int, str, float, list, tuple}

    if type(self) in you_cant:
        raise TypeError("can't add new attribute")

    self.__setattr__(name, value)
