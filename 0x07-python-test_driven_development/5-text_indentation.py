#!/usr/bin/python3
"""
Text indentation
"""

def text_indentation(text):
    """
    function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    n_txt = text.replace('?', '?\n\n')
    n_txt = n_txt.replace('.', '.\n\n')
    n_txt = n_txt.replace(':', ':\n\n')

    print("\n".join([li.strip() for li in n_txt.split("\n")]), end="")
