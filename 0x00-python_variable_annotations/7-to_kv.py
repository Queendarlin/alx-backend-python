#!/usr/bin/env python3
"""
Module of  a function that returns a tuple
with a string and the square of an int or float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string k and an int or float v and returns a tuple.

    Args:
    k (str): A string.
    v (Union[int, float]): An integer or float.

    Returns:
    Tuple[str, float]: A tuple containing the string
    and the square of the int/float.
    """
    return (k, float(v ** 2))
