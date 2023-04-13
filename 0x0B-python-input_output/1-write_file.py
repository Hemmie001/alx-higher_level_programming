#!/usr/bin/python3
"""Write to a file"""


def number_of_lines(filename="", text=""):
    """ writes a string to a text file (UTF8)
    and returns the number of characters written"""
    with open(filename, mode="r", encoding="utf-8") as text_file:
        counter = 0
        for line in text_file:
            counter += 1
    text_file.close()
    return counter
