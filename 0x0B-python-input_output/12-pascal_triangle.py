#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the Pascal’s triangle
    """

    if n <= 0:
        return []
    lista = [[1]]
    tmp = []
    for i in range(n - 1):
        tmp = tmp.copy()
        tmp = []
        tmp.append(1)
        for j in range(i):
            tmp.append(lista[i][j] + lista[i][j + 1])
        tmp.append(1)
        lista.append(tmp)
    return listaie
