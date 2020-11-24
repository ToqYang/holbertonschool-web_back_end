#!/usr/bin/env python3
""" Test utils
"""
import unittest
from unittest.mock import patch
import requests
from utils import access_nested_map, get_json
from parameterized import parameterized, parameterized_class


class TestAccessNestedMap(unittest.TestCase):
    """ Access nested map """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path_map, result_expec):
        """ Access nested method

            args:
                nested_map: {"a": 1},
                path: ("a",)
                result_expec: 1

            return
                Ok if its correct
        """
        self.assertEqual(access_nested_map(nested_map, path_map), result_expec)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path_map):
        """ Exception access nested method

            args:
                nested_map: {}
                path: ("a",)

            return:
                ok if its correct
        """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path_map)

        self.assertEqual(
            f'KeyError({str(error.exception)})', repr(error.exception))


class TestGetJson(unittest.TestCase):
    """ Test JSON """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Mock HTTP calls

            args:
                url: Web page to look
                response: result of the consult
        """
        conf = {'return_value.json.return_value': test_payload}
        patcher = patch('requests.get', **conf)
        mock = patcher.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()
        patcher.stop()
