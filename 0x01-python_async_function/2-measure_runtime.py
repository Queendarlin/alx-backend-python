#!/usr/bin/env python3
"""
Module for measure_time function
"""
import time
import asyncio
from typing import List

# Import wait_n from the previous file
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n.

    Args:
        n (int): Number of times to call wait_random.
        max_delay (int): Maximum delay for each wait_random call.

    Returns:
        float: Average time per coroutine call.
    """
    start_time = time.perf_counter()  # Start measuring time
    asyncio.run(wait_n(n, max_delay))  # Execute the wait_n function
    end_time = time.perf_counter()  # End measuring time

    total_time = end_time - start_time  # Calculate total elapsed time
    return total_time / n  # Return average time per coroutine
