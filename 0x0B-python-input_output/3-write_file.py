#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8) 
    and returns the number of characters written
    Args:
    filename: current file name.
    text: text that would be written in the file.
    Return: Nbr of characters written in the text.
    """

    with open(filename, encoding="utf-8", mode="w") as f:
        return f.write(text)
