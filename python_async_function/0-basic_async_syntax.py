#!/usr/bin/env python3
"""
Provides an asynchronous coroutine that waits
for a random delay and returns it.
"""
import random
import asyncio


async def wait_random(max_delay=10) -> float:
    """
    Asynchronous coroutine that waits for a random delay
    between 0 and max_delay seconds.

    Args:
        max_delay (int): The maximum delay time in
        seconds. Default is 10.

    Returns:
        float: The actual delay time in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
