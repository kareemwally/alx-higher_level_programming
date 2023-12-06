#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = [[row[i] ** 2 for i in range(len(row))] for row in matrix]
    return res
