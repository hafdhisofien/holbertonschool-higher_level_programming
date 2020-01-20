#!/usr/bin/python3
"""
Print square
"""


def print_square(size):
    """function that prints a square with the character #
    """
    if not isinstance(size, int):
        if not isinstance(size, float):
            raise TypeError("size must be an integer")
        elif isinstance(size, float) and size > 0:
            size = int(size)
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        for y in range(size):
            print('#', end="")
        print()
