#!/usr/bin/env python3
"""
Async Comprehension Module

This module contains a coroutine that collects 10 random numbers using an async
comprehension over the async_generator and returns them.
"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    async_comprehension

    Collects 10 random numbers from async_generator using async comprehension.

    Returns:
        List[float]: A list of 10 random float numbers.
    """
    return [number async for number in async_generator()]
