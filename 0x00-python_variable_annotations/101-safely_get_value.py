#!/usr/bin/env python3
"""
This module contains a function to safely retrieve a value from a dictionary
or return a default value.
"""

from typing import Mapping, Any, Union, TypeVar

# Define a TypeVar for the default value
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves the value associated with key from dct,
    or returns default if key is not in dct.

    Args:
    dct (Mapping): A mapping (e.g., dictionary) where key is looked up.
    key (Any): The key to lookup in dct.
    default (Union[T, None], optional): The default value
    to return if key is not found in dct. Defaults to None.

    Returns:
    Union[Any, T]: The value associated with key in dct if it exists,
    otherwise default.
    """
    if key in dct:
        return dct[key]
    else:
        return default
