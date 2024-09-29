#!/usr/bin/python3
"""
testing a method for getting the max number of list
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMax_Integer(unittest.TestCase):
    """
    class including the main functions for testing the method
    """

    def test_regularcase(self):
        """ testing regular cases with a int list """
        self.assertEqual(max_integer([50]), 50)
        self.assertEqual(max_integer([-100, -60, -1, 0]), 0)
        self.assertEqual(max_integer([50.9, 60, 100.2, 100.5]), 100.5)
        self.assertEqual(max_integer([4, 12, 9 * 2]), 18)
        self.assertEqual(max_integer([4, 12, 9 * 2]), 18)
        self.assertEqual(max_integer([0.1, 0.2, 0.15]), 0.2)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([50.9, True]), 50.9)

    def test_type(self):
        """ testing the type of the list"""
        self.assertEqual(max_integer((50.9, 60, 100.2, 100.5)), 100.5)
        self.assertEqual(max_integer(()), None)
        with self.assertRaises(TypeError, msg="'>' not supported between instances of 'list' and 'int'"):
            max_integer([10, 5, [2, 3]])
        with self.assertRaises(TypeError, msg="'>' not supported between instances of 'str' and 'int'"):
            max_integer([1, 2, 's'])

        with self.assertRaises(TypeError, msg="object of type 'int' has no len()"):
            max_integer((50))
