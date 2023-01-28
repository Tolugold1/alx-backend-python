#!/usr/bin/env python3
""" unit test for utils.access_nested_map"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """testing utils.access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, m_param, m_path, expected):
        """test if mapping_param equalls the expected value/mapping path"""
        self.assertEqual(access_nested_map(m_param, m_path), expected)
    
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """test if an exception is raised"""
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)
        self.assertEqual(err.exception.args[0], path[-1])

class TestGetJson(unittest.TestCase):
    """testing get_json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("test.get_json")
    def test_get_json(self, t_url, p_payload, mock_get):
        """testing get_json to see if it returns the expected value"""
        mock_get.return_value = p_payload
        value = get_json(t_url)
        self.assertEqual(value, p_payload)

class TestMemoize(unittest.TestCase):
    """ TESTCASE """
    def test_memoize(self):
        """ Test that when calling a_property twice, the correct result is
            returned but a_method is only called once using assert_called_once
        """
        class TestClass:
            """ class """
            def a_method(self):
                """ method  """
                return 42

            @memoize
            def a_property(self):
                """ property """
                return self.a_method()
        with patch.object(TestClass, "a_method") as mockMethod:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            mockMethod.assert_called_once
