#!/usr/bin/env python3
"""
Modules who import previous function and return number in a list.
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers asynchronously using async comprehension.

    Uses async_generator to yield values and returns them as a list.

    Returns:
        A list of 10 float values collected from async_generator.
    """
    return [gen_float async for gen_float in async_generator()]
