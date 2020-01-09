#!/usr/bin/python3
class Square:
     """" A simple Square"""

     def __init__(self, size=0):
         self.__size = size
         try:
             size += 1
             if (size<0):
                 raise ValueError
         except ValueError:
             raise Exception("size must be >= 0")
         except TypeError:
             raise Exception("size must be an integer")
