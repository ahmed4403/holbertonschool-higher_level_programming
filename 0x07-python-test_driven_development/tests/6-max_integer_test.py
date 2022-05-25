#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    This is a class
    that is a class
    which is a class
    """
    def test_max_integer(self):
        """
        This is a function
        that is a function
        which is a function
        """
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([-3, -2, -1]), -1)
        self.assertAlmostEqual(max_integer([-3.5, -2.5, -1.5]), -1.5)
        self.assertAlmostEqual(max_integer([1.22, 1.23, 1.24, 1.25]), 1.25)
        self.assertAlmostEqual(max_integer([1, 10, 4.5, 1.25]), 10)
        self.assertAlmostEqual(max_integer([534, 343, 3301, 53, 352]), 3301)
        self.assertEqual(max_integer([50, 40, 30, 20,]), 50)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 1, 1, 1, 1]), 1)
        self.assertEqual(max_integer("hello"), "o")
        self.assertEqual(max_integer(["h", "e", "l", "l", "o"]), "o")
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([]), None)
        with self.assertRaises(TypeError):
            max_integer([1, 2, "hello"])
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3], 4)
