#!/usr/bin/python3
def safe_print_integer(value):
    "prints an integer with '{:d}'.format()"
    try:
        print("{:d}".format(value))
        return True
    # Do not leave your except bare.
    # Specify exception instead.
    except(TypeError, ValueError):
        return False
