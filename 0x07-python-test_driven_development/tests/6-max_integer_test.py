#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def empty_list_test(self):
        self.assertEqual(max_integer([]), None)

    def nagative_test(self):
        my_list = [-1, -22, -3, -4]
        self.assertEqual(max_integer(my_list), -1)

    def mixed_test(self):
        my_list = [2, 3, 4, 5, 'd']
        self.assertEqual(max_integer(my_list), "d")

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def with_string(self):
        self.assertEqual(max_integer("string"), "f")
