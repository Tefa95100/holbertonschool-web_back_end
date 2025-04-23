#!/usr/bin/env python3
"""
Provides an asynchronous function to run multiple
task_wait_random concurrently.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the
    specified max_delay and returns the delays.

    Args:
        n (int): Number of tasks to run.
        max_delay (int): Maximum delay for each task.

    Returns:
        List[float]: List of delay times in ascending order.
    """
    delays = []
    for coro in asyncio.as_completed([task_wait_random(max_delay)
                                      for _ in range(n)]):
        delay = await coro
        delays.append(delay)
    return delays
