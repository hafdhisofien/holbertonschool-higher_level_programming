#!/usr/bin/python3
def number_of_lines(filename=""):
    """
    function that returns the number of lines of a text file
    Args:
    Count = number of lines to be returned
    """
    count = 0
    with open(filename) as f:
        for lines in f:
            count += 1
        return (count)
