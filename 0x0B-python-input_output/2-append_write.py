#!/usr/bin/python3
"""2-Append to a file"""

def read_lines(filename="", text="", nb_lines=0):
    """appends a string at the end of a text file (UTF8)
    and returns the number of characters added:"""
    with open(filename, mode="r", encoding="utf-8") as text_file:
        counter = 0
        for line in text_file:
            if counter == nb_lines and nb_lines > 0:
                break
            print(line, end="")
            counter += 1
    text_file.close()
