#!/usr/bin/env python3
"""
Async Generator Module

This module contains an asynchronous generator coroutine that yields random
floating-point numbers between 0 and 10, with a 1-second delay between yields.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    async_generator

    Asynchronous generator that yields random floating-point numbers between
    0 and 10.

    Yields:
        float: A random float number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
