#!/usr/bin/env python3

"""
This module contains unit tests for the `utils.access_nested_map` function.
"""

import unittest
from typing import Dict, Tuple, Any
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for the `access_nested_map` function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
        self,
        nested_map: Dict[str, Any],
        path: Tuple[str, ...],
        expected: Any
    ) -> None:
        """
        Test the `access_nested_map` function with various inputs.

        Args:
        nested_map (Dict[str, Any]): The nested dictionary to test.
        path (Tuple[str, ...]): The path to access in the nested dictionary.
        expected (Any): The expected result from the function.

        Returns:
            None
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map: Dict[str, Any],
                                         path: Tuple[str, ...]) -> None:
        """
        Test access_nested_map raises KeyError for invalid paths.

        Args:
            nested_map (dict): The nested map to access.
            path (tuple): The path to the value in the nested map.
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), str(KeyError(path[-1])))


if __name__ == '__main__':
    unittest.main()
