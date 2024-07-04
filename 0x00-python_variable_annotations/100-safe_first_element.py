#!/usr/bin/env python3
"""
This module contains a function to safely return the first element of a
sequence or None if the sequence is empty.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Takes a sequence lst and returns its first element if it exists,
    otherwise returns None.

    Args:
    lst (Sequence[Any]): A sequence (list, tuple, etc.)
    containing elements of any type.

    Returns:
    Union[Any, None]: The first element of lst if lst is not empty,
    otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
