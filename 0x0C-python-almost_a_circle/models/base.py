#!/usr/bin/python3
"""This class will be the “base” of all other classes in this project
"""


class Base:
    """
    the goal of this class is to manage
    id attribute in all your future classes
    and to avoid duplicating the same code
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
