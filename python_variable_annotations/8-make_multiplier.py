#!/usr/bin/env python3
"""
Contains a function that returns a multiplier function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier to apply.

    Returns:
        Callable[[float], float]: A function that multiplies
        its input by multiplier.
    """
    def multiply(number: float) -> float:
        """
        Multiplies the input number by the captured multiplier.

        Args:
            number (float): The number to be multiplied.

        Returns:
            float: The result of the multiplication.
        """
        return number * multiplier
    return multiply
