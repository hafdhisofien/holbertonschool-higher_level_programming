#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """
    function that reads n lines of a text file (UTF8) and prints it to stdout
    Args:
    filename: current file name
    nb_lines: number of line currently reading
    Return: None
    """
    count = 0
    with open(filename, encoding="utf-8") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        else:
            for f in f:
                if count < nb_lines:
                    print(f, end="")
                count += 1
