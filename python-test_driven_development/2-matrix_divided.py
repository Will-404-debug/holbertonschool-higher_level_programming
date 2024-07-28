#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): List of lists of integers/floats.
        div (int/float): The divisor.

    Returns:
        list of lists: New matrix with elements divided by div, rounded to 2 decimals.

    Raises:
        TypeError: If matrix elements are not lists of integers/floats, or if div is not a number.
        TypeError: If rows of the matrix are not the same size.
        ZeroDivisionError: If div is zero.
    """
    if matrix is None or div is None:
        raise TypeError("matrix_divided() missing 1 required positional argument: 'matrix' or 'div'")
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
