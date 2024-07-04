#!/usr/bin/env python3
from typing import List

"""Module of a function that sums a list of floats"""


def sum_list(input_list: List[float]) -> float:
    """
    Takes a list of floats and returns their sum.

    Args:
    input_list (List[float]): A list of floats.

    Returns:
    float: The sum of the floats in the list.
    """
    return sum(input_list)
