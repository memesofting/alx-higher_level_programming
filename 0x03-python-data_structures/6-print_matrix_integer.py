#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        return None
    else:
        for i in range(len(matrix)):
            row = matrix[i]
            for j in range(len(row)):
                if j == len(row) - 1:
                    print("{:d}".format(row[j]))
                else:
                    print("{:d} ".format(row[j]), end="")
