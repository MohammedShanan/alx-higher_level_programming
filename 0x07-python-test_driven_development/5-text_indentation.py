#!/usr/bin/python3
"""
Module 5-text_indentation
Contains method that prints text with 2 new lines after each ".", "?", and ":"
Takes in a string
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each ".", "?", and ":"
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in "?.:":
        text = text.replace(char, char + "\n\n")
    text = [line.strip(" ") for line in text.split("\n")]
    text = "\n".join(text)
    print(text, end="")
