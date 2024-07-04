#!/usr/bin/env python3
"""
Module for a function to zoom in an array-like structure by repeating elements
"""

from typing import List, Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Zooms in on the elements of the input tuple by repeating each element.

    Args:
        lst (Tuple[int, ...]): The input tuple containing integers.
        factor (int): The factor by which to repeat each element. Default is 2

    Returns:
        List[int]: A list with each element of the input tuple
        repeated by the given factor.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array: Tuple[int, ...] = (12, 72, 91)

zoom_2x: List[int] = zoom_array(array)
zoom_3x: List[int] = zoom_array(array, 3)
