#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    length = len(matrix)
    for i in range(length):
        for j in range(len(matrix[0])):
            res[i][j] = matrix[i][j] ** 2
    return res
