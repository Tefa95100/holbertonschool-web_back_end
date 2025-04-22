#!/usr/bin/python3
""""
Module that defines a function to compute the length
of elements in an iterable of sequences.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples.
    Each tuple contains the element and its length.

    Args:
        lst (Iterable[Sequence]): An iterable containing
        sequence-like elements (e.g. strings, lists, tuples).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples
        with each element and its length.
    """
    return [(i, len(i)) for i in lst]
