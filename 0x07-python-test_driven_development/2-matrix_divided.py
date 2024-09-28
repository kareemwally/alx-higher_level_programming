#!/usr/bin/python3
"""
a simple function to divide a 2D array `matrix` by a number `div`
"""

Errors_msgs = [
        "div must be a number",
        "division by zero",
        "Each row of the matrix must have the same size",
        "matrix must be a matrix (list of lists) of integers/floats"
        ]


def matrix_divided(matrix, div):
    """
    matrix must be a square 2D array of real numbers
    and div must be a real positive number
    """
    if type(div) not in [int, float]:
        raise TypeError(Errors_msgs[0])

    if div == 0:
        raise ZeroDivisionError(Errors_msgs[1])

    size = len(matrix[0])
    res = []
    for array in matrix:
        if size != len(array):
            raise TypeError(Errors_msgs[2])
        for ele in array:
            if type(ele) not in [float, int]:
                raise TypeError(Errors_msgs[3])
        res.append([round(ele/div, 2) for ele in array])

    return res
