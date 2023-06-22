#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        raw = []
        for j in i:
            j = j * j
            raw.append(j)
        new_matrix.append(raw)
    return new_matrix
