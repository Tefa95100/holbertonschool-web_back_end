#!/usr/bin/python3
"""
Module contain a function for add all element in a list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
	"""
    Returns the sum of a list containing integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing int and float values.

    Returns:
        float: The total sum of the elements as a float.
    """
	return sum(mxd_lst)
