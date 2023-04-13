#!/usr/bin/python3
"""2-Append to a file"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)
    and returns the number of characters added:"""
    with open(filename, 'a', encoding='utf=8') as text_file:
        return text_file.write(text)