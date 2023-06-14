#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_matrix = []
    for row in matrix:
        n_matrix.append([number ** 2 for number in row])
    return n_matrix
