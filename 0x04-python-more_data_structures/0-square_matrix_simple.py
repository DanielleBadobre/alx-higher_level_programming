#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def square_func(x):
        return x ** 2
    square_matrix = []
    for row in matrix:
        square_row = list(map(square_func, row))
        square_matrix.append(square_row)
    return square_matrix
