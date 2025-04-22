#!/usr/bin/python3
"""
Return the floor of floating number.
"""
import math


def floor(n: float) -> int:
    """
    Returns the floor of a float.
    The floor is the greatest integer less than or equal to the input number.

    Args:
        n (float): the float

    Returns:
        int: The largest integer less than or equal to n.
    """
    return math.floor(n)
