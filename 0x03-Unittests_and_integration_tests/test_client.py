#!/usr/bin/env python3
"""
This module contains unit tests for the client module.
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    This class contains unit tests for the GithubOrgClient class.
    """

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json) -> None:
        """
        Test that GithubOrgClient.org returns the correct value.
        """
        test_payload = {"login": org_name}
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, test_payload)
        (mock_get_json.assert_called_once_with
         (f'https://api.github.com/orgs/{org_name}'))

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org: PropertyMock) -> None:
        """
        Test that GithubOrgClient._public_repos_url returns the correct value.
        """
        test_payload = {"repos_url": "https://api.github.com/orgs/test/repos"}
        mock_org.return_value = test_payload

        client = GithubOrgClient("test")
        self.assertEqual(client._public_repos_url, test_payload["repos_url"])


if __name__ == '__main__':
    unittest.main()
