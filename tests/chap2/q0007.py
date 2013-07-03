#!/usr/bin/python


import unittest

from exercises.chap2 import q0007


class TestCase(unittest.TestCase):
    def test_docstring(self):
        self.assertIsNotNone(q0007.wordcount.__doc__)

    def test_empty(self):
        r = q0007.wordcount([])
        self.assertEqual({}, r)

    def test_some(self):
        xs = ['a', 'b', 'a', 'a', 'c']
        r = q0007.wordcount(xs)
        self.assertEqual({'a': 3, 'b': 1, 'c': 1}, r)

    def test_k(self):
        xs = ['a' for i in range(1000)]
        r = q0007.wordcount(xs)
        self.assertEqual({'a': 1000}, r)


if __name__ == '__main__':
    unittest.main()
