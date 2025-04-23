#!/usr/bin/env python3
"""
Provides an asynchronous coroutine that runs
multiple wait_random coroutines concurrently.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified
    max_delay and return the list of delays.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay time for each wait_random call.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = []
    """
    coro = coroutine is a convention for async,
    _ = it's when the variable is not use
    """
    for coro in asyncio.as_completed([wait_random(max_delay)
                                      for _ in range(n)]):
        delay = await coro
        delays.append(delay)
    return delays
