#!/usr/bin/python


import unittest

from exercises.chap2 import q0006


data = [1, 0, False, True, [], (1, ), [0, ], {}, set(), set([1]), 100]


class TestCase(unittest.TestCase):
    def test_docstring(self):
        self.assertIsNotNone(q0006.false_only.__doc__)

    def test_empty(self):
        self.assertEqual([], q0006.false_only([]))

    def test_xs(self):
        xs = q0006.false_only(data)
        for x in xs:
            self.assertFalse(x)

if __name__ == '__main__':
    unittest.main()
