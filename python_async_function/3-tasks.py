#!/usr/bin/env python3
"""
Provides a function that returns an asyncio.
Task wrapping wait_random coroutine.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task that runs the wait_random coroutine.

    Args:
        max_delay (int): Maximum delay time for wait_random.

    Returns:
        asyncio.Task: Task object wrapping the coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
