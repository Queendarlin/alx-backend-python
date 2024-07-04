#!/usr/bin/env python3
"""
This module contains a function to return a list of tuples
containing elements and their lengths.
"""

from typing import Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples
    where each tuple contains an element from lst and its length.

    Args:
    lst (Iterable[Sequence]): An iterable containing sequences
    (e.g., list, tuple, string).

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples
    where each tuple contains an element from lst
    and its length.
    """
    return [(i, len(i)) for i in lst]
