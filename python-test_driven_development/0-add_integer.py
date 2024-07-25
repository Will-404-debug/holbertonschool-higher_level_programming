#!/usr/bin/python3

"""
Module for adding two integers.

This module provides a function `add_integer` that adds two numbers
and returns the result as an integer. It performs type checking and
casts float inputs to integers.
"""

def add_integer(a, b=98):
    """Add two integers.

    Parameters:
    a (int, float): The first number to be added.
    b (int, float): The second number to be added, default is 98.

    Returns:
    int: The sum of a and b after casting them to integers.

    Raises:
    TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
