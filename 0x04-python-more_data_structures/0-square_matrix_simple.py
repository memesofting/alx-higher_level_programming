#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    if matrix is not None:
        for i in matrix:
            new_row = []
            for j in i:
                new_row.append(j ** 2)
            new.append(new_row)
    return new
