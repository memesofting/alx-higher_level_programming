#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy = []
    if matrix != None:
        copy = matrix.copy()
    for i in range(len(matrix)):
        for j in matrix[i]:
            copy.append(j ** 2)
    return copy
