#!/usr/bin/env python3

"""
This module contains unit tests for the `utils.access_nested_map` function.
"""

import unittest
from typing import Dict, Tuple, Any
from utils import access_nested_map
from parameterized import parameterized
from utils import get_json
from unittest.mock import patch, Mock
from utils import memoize


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


class TestGetJson(unittest.TestCase):
    """
    This class contains unit tests for the get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str,
                      test_payload: Dict[str, bool]) -> None:
        """
        Test get_json returns the correct result.

        Args:
            test_url (str): The URL to send the request to.
            test_payload (dict): The expected payload returned by the request.
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch('utils.requests.get',
                   return_value=mock_response) as mock_get:
            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    This class contains unit tests for the memoize decorator.
    """

    def test_memoize(self) -> None:
        """
        Test memoize decorator works as expected.
        """

        class TestClass:
            def a_method(self) -> int:
                return 42

            @memoize
            def a_property(self) -> int:
                return self.a_method()

        with patch.object(TestClass, 'a_method',
                          return_value=42) as mock_method:
            test_instance = TestClass()
            self.assertEqual(test_instance.a_property, 42)
            self.assertEqual(test_instance.a_property, 42)
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
