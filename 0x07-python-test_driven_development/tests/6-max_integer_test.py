#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def setUp(self):
        self.li = [1, 2, 3, 4]
        self.li_str = [1, 2, "A", 3]

    def test_maxinlist(self):
        self.assertEqual(max_integer(self.li), 4)

    def test_strinlist(self):
        #test list contain strings
        self.assertRaises(TypeError, max_integer(self.li_str))


if __name__ == '__main__':
    unittest.main()
