#!/usr/bin/python3
"""Unit tests for Square."""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_square_creation(self):
        s = Square(5)

        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_size(self):
        s = Square(5)

        self.assertEqual(s.size, 5)

        s.size = 10

        self.assertEqual(s.size, 10)

    def test_invalid_size(self):
        with self.assertRaises(TypeError):
            Square("5")

    def test_dictionary(self):
        s = Square(5)

        dictionary = s.to_dictionary()

        self.assertEqual(dictionary["size"], 5)

    def test_update(self):
        s = Square(5)

        s.update(89, 2, 3, 4)

        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)


if __name__ == "__main__":
    unittest.main()
