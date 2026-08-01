#!/usr/bin/python3
"""Unit tests for Base."""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_id_auto(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_given(self):
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json(self):
        result = Base.to_json_string([{"id": 12}])
        self.assertIsInstance(result, str)

    def test_from_json_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json(self):
        result = Base.from_json_string('[{"id": 89}]')
        self.assertIsInstance(result, list)


if __name__ == "__main__":
    unittest.main()
