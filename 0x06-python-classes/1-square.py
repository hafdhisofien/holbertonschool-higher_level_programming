#!/usr/bin/python3
class Square:
     """" A simple Square"""

     def __init__(self, size):
          """Example function with types documented in the docstring.
          `PEP 484`_ type annotations are supported. If attribute, parameter, and
          return types are annotated according to `PEP 484`_, they do not need to be
          included in the docstring:
          Args:
          self: self.
          size: Private instance attribute.
          """
          self.__size = size
