#!/usr/bin/python3
"""Module for the division of ol the elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Function to divide all the elements of a matrix
    :param matrix: matrix to divide
    :param div: divider
    :return: a matrix made of all the divisions results
    """
    first_row = len(matrix[0])
    for row in matrix[1:]:
        if len(row) != first_row:
            raise TypeError("Each row of the matrix must have the same size")
    for rows in matrix:
        for element in rows:
            if type(element) != int and type(element) != float:
                raise TypeError(
                        "matrix must be a matrix" + "" +
                        "(list of lists) of integers/floats"
                )
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    div_matrix = [[round(element/div, 2) for element in row] for row in matrix]
    return div_matrix
