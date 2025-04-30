#!/usr/bin/env python3
"""
Modules who import previous module and measure the total runtimes
for running four time asyn_comprehension in parallel.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of running async_comprehension
    four times in parallel.

    Uses asyncio.gather to run the coroutines concurrently.
    Since each async_comprehension takes ~10 seconds, and they run in parallel,
    the total runtime should be close to 10 seconds.

    Returns:
        The total execution time in seconds (as a float).
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
