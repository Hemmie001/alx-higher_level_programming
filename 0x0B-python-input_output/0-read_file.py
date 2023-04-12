#!/usr/bin/python3
"""0. Read file"""


def read_file(filename=""):
    """ reads a text file (UTF8) and prints it to stdout"""
    with open(filename, mode="r", encoding="utf-8") as text_file:
        print(text_file.read(), end="")
