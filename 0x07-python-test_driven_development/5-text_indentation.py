#!/usr/bin/python3
""" This module contains only one function """


def text_indentation(text):
    """ prints a text with 2 new lines after each of these
    characters: ., ? and :

    Args:
       text (str): a string text.
    Raises:
       TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    cha = 0

    while cha < len(text) and text[cha] == ' ':
        cha += 1

    while cha < len(text):
        print(text[cha], end="")
        if text[cha] == "\n" or text[cha] in ".?:":
            if text[cha] in ".?:":
                print("\n")
            cha += 1
            while cha < len(text) and text[cha] == ' ':
                cha += 1
            continue
        cha += 1
