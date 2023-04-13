#!/usr/bin/python3
"""Write to a file"""


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8)
    and returns the number of characters written"""
    with open(filename, mode="w", encoding="utf-8") as text_file:
        characters = text_file.write(text)
    text_file.close()
    return characters
