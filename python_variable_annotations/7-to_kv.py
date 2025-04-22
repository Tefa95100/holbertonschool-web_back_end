#!/usr/bin/python3
"""
Module contain a function who accep a string and a number
before return the square of this number in float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with a string and the square of a number (as float).

    Args:
        k (str): The string key.
        v (Union[int, float]): A number (int or float).

    Returns:
        Tuple[str, float]: A tuple where the first element
        is k and the second is v squared.
    """
    return (k, float(v ** 2))
