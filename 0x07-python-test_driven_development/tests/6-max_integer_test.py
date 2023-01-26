#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInt(unittest.TestCase):
    """run test with python3 -m unittest -v tests.6-max_integer_test"""

    def test_module_doc_string(self):
        module_doc = __import__('6-max_integer').__doc__
        self.assertTrue(len(module_doc) > 1)

    def test_fuction_doc_string(self):
        func_doc = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(func_doc) > 1)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(""), None)

    def test_int_float(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 7, 3, 4]), 7)
        self.assertEqual(max_integer([1, -7, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -7, -3, -4]), -1)

    def test_strings(self):
        self.assertEqual(max_integer("1234"), '4')
        self.assertEqual(max_integer("1732"), '7')
        self.assertEqual(max_integer("xyz"), 'z')
        self.assertEqual(max_integer("xyz"), 'z')

    def test_errors(self):
        with self.assertRaises(TypeError):
            max_integer({1, 2}, {3, 4, 5})
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, "4"])
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == "__main__":
    unittest.main()
