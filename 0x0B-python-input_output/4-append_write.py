#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    Args:
    filename: current file name.
    text: text that would be written in the file.
    Return: the number of characters added.
    """
    with open(filename, encoding="utf-8", mode="a") as f:
        return f.write(text)
