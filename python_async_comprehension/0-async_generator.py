#!/usr/bin/env python3
"""
Module with a function for generate 10 numbers
between 0 and 10.
"""
import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously yield 10 random numbers between 0 and 10.

    This coroutine waits for 1 second before yielding each number.

    Returns:
        An asynchronous generator that yields 10 float values between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
