#!/usr/bin/python3


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): A matrix represented as a list of lists of integers or floats.
        div (int/float): The divisor.

    Returns:
        list of lists: A new matrix with each element divided by div and rounded to 2 decimal places.

    Raises:
        TypeError: If matrix elements are not lists of integers/floats or if div is not a number.
        TypeError: If the rows of the matrix are not of the same size.
        ZeroDivisionError: If div is zero.
    """
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
