#!/usr/bin/env python3
"""
Provides a function to measure the average runtime of wait_n.
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average execution time of wait_n.

    Args:
        n (int): Number of coroutines to run.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        float: Average time per coroutine.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n
