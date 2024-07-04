#!/usr/bin/env python3
"""
This module contains a function that returns a function
to multiply a float by a given multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier and returns a function that
    multiplies a float by the multiplier.

    Args:
    multiplier (float): The multiplier to use for multiplication.

    Returns:
    Callable[[float], float]: A function that takes a float
    and returns its product with multiplier.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
