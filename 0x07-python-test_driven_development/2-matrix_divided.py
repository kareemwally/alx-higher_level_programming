#!/usr/bin/python3
"""
a simple function to divide a 2D array `matrix` by a number `div`
"""


def matrix_divided(matrix, div):
    """
    matrix must be a square 2D array of real numbers
    and div must be a real positive number
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    size = len(matrix[0])
    res = []
    for array in matrix:
        if size != len(array):
            raise TypeError("Each row of the matrix must have the same size")
        for ele in array:
            if type(ele) not in [float, int]:
                raise TypeError("matrix must be a matrix(list of lists)\
                        of integers/floats")
        res.append([round(ele/div, 2) for ele in array])

    return res
