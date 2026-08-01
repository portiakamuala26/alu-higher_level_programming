#!/usr/bin/python3
"""Unit tests for Rectangle."""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_rectangle_creation(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_invalid_width(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_invalid_height(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_display(self):
        r = Rectangle(2, 2)
        self.assertIsNone(r.display())

    def test_update(self):
        r = Rectangle(1, 1)
        r.update(89, 2, 3, 4, 5)

        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_dictionary(self):
        r = Rectangle(1, 2)
        dictionary = r.to_dictionary()

        self.assertEqual(dictionary["width"], 1)
        self.assertEqual(dictionary["height"], 2)


if __name__ == "__main__":
    unittest.main()
