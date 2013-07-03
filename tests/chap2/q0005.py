#!/usr/bin/python


import unittest

from exercises.chap2 import q0005


class NumberingTestCase(unittest.TestCase):
    def test_docstring(self):
        self.assertIsNotNone(q0005.numbering.__doc__)

    def test_empty(self):
        self.assertEqual([], q0005.numbering([]))

    def test_justOne(self):
        self.assertEqual([(0, 'Zero')], q0005.numbering(['Zero']))

    def test_count(self):
        k = q0005.numbering(list(range(1000)))
        self.assertEqual(1000, len(k))
        for i in range(1000):
            self.assertEqual((i, i), k[i])


if __name__ == '__main__':
    unittest.main()
