#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for i in matrix:
        if len(i):
            for j in i[:-1]:
                print("{:d}".format(j), end=' ')
            print("{}".format(i[-1]))
