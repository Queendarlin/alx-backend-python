#!/usr/bin/env python3
"""
Module for to_str function with type annotations.
"""


def to_str(n: float) -> str:
    """
    Returns the string representation of a floating point number.

    Args:
        n (float): The number to convert to string.

    Returns:
        str: The string representation of the number.
    """
    return n.__str__()
