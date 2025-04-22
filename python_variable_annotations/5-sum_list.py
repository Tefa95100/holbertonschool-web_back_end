#!/usr/bin/python3
"""
module contain one function sum list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Function add all float of a list and return a float

    Args:
        input_list (list[float]): A list of float

    Returns:
        float: Sum of all float in the list
    """
    return sum(input_list)
