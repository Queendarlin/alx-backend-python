#!/usr/bin/env python3
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list of integers and floats and returns their sum as a float.

    Args:
    mxd_lst (List[Union[int, float]]): A list of integers and floats.

    Returns:
    float: The sum of the numbers in the list.
    """
    return sum(mxd_lst)
