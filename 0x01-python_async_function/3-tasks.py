#!/usr/bin/env python3
"""
Module for task_wait_random function
"""
import asyncio
from typing import Coroutine

# Import wait_random from 0-basic_async_syntax
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task that runs wait_random(max_delay).

    Args:
        max_delay (int): Maximum delay value for wait_random.

    Returns:
        asyncio.Task: Task object representing the execution of wait_random.
    """
    # Create a task using asyncio.create_task
    task = asyncio.create_task(wait_random(max_delay))
    return task
