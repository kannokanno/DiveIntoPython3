#!/usr/bin/python


import unittest

from exercises.chap2 import q0008


class TestCase(unittest.TestCase):
    def test_docstring(self):
        self.assertIsNotNone(q0008.flatten.__doc__)

    def test_empty(self):
        self.assertEqual([], q0008.flatten([]))

    def test_single(self):
        self.assertEqual([1], q0008.flatten([1]))

    def test_simple(self):
        self.assertEqual([1, 2, 3], q0008.flatten([1, 2, 3]))

    def test_example(self):
        self.assertEqual([1, 2, 3], q0008.flatten([[1, 2], 3]))

    def test_various_types(self):
        self.assertEqual(
            [1, 'a', True, {}, (), set([1, 2])],
            q0008.flatten([[1, 'a'], [[True, {}], ()], set([1, 2])]))

    def test_200times_nested(self):
        r = [1, 2]
        for i in range(200):
            r = [r]
        self.assertEqual([1, 2, 3], q0008.flatten([r, 3]))


if __name__ == '__main__':
    unittest.main()
