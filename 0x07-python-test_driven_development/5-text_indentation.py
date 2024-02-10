#!/usr/bin/python3
"""Module that prints a text"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines after certain chars
    :param text: text to print
    :return: nothing
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    skip_space = False
    for char in text:
        if (char == "?") or (char == ":") or (char == "."):
            print(char, end="\n\n")
            skip_space = True
        elif char == " " and skip_space:
            continue
        else:
            print(char, end="")
            skip_space = False
