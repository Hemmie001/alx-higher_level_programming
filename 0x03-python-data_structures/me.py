#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in m atrix:
        for c ol in row:
            print("{:d}".format(col), end=" " if col != row[-1] else "")
        print()
