#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ unittest for max integer """
    def test_docstring(self):
        """module docstring test """
        length = __import__('6-max_integer').__doc__
        self.assertTrue(len(length) > 1)

    def test_func_docsring(self):
        """ function docstring test """
        length2 = max_integer.__doc__
        self.assertTrue(len(length2) > 1)

    def test_max_middle(self):
        """ tests if max is in middle """
        a = [34, 45, 95, 10, 28]
        self.assertEqual(max_integer(a), 95)

    def test_max_begin(self):
        """tests if max is in the beginning """
        b = [95, 34, 45, 10, 28]
        self.assertEqual(max_integer(b), 95)

    def test_max_end(self):
        """ tests if max at end """
        c = [34, 45, 10, 28, 95]
        self.assertEqual(max_integer(c), 95)

    def test_empty(self):
        """ tests for empty list """
        d = []
        self.assertIsNone(max_integer(d))

    def test_nonint(self):
        """ tests if non integer list """
        e = [34, 45, "noah", 15, 20]
        with self.assertRaises(TypeError):
            max_integer(e)

    def test_negative(self):
        """ test for negative numbers """
        f = [-34, -45, -10, -28, -95]
        self.assertEqual(max_integer(f), -10)

    def test_none(self):
        """ test if none """
        with self.assertRaises(TypeError):
            max_integer(None)

if __name__ == "__main__":
    unittest.main()
