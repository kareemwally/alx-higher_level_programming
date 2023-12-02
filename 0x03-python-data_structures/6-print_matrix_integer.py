#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for i in matrix:
        if not len(i):
            return print()
        for j in i[:-1]:
            print("{:d}".format(j), end=' ')
        print("{:d}".format(i[-1]))
