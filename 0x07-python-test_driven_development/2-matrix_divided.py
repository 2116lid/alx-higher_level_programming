#!/usr/bin/python3

""" This module is 2-matrix_divided """



def matrix_divided(matrix, div):
    """ Returns the division of the list.
    Args:
       matrix (list):  list of lists of integers or floats.
       div (int or float): divisor.
    Raises:
         TypeError: If matrix doesn't contain int/floats.
         TypeError: If Each row of matrix is not the same size.
         TypeError: If div is not a number.
         ZeroDivisionError: If div is equal to 0.
    Returns:
        a new matrix.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(el, int) or isinstance(el, float)) for
                el in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
