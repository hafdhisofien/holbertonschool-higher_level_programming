#!/usr/bin/python3
"""
Divide a matrix
"""

def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix
    """
    len_m = len(matrix)
    new_m = []
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        for item in matrix:
            for i in range(len(item)):
                if type(item[i]) is not int and type(item[i]) is not float:
                    raise TypeError("matrix must be a matrix (list of lists) \
                            of integers/floats")
            new_m.append(list(map(lambda x: round(x / div, 2), item)))
        if len_m != len(new_m):
            raise TypeError("Each row of the matrix must have the same size")
        return new_m
