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
        self.assertEqual(max_integer([-100, -60, -1, 0,]), 0)
        self.assertEqual(max_integer([50.9, 60, 100.2, 100.5,]), 100.5)
        self.assertEqual(max_integer([4, 12, 9 * 2]), 18)
        self.assertEqual(max_integer([0.1, 0.2, 0.3, 0.35,]), 0.35)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([50.9,True]), 50.9)

    def test_type(self):
        """ testing the type of the list""" 
        self.assertEqual(max_integer((50.9, 60, 100.2, 100.5)), 100.5)
        self.assertEqual(max_integer(()), None)


