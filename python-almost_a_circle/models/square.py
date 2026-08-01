#!/usr/bin/python3
"""Defines the Square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the string representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.size
        )

    @property
    def size(self):
        """Gets the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the Square."""
        self.width = value
        self.height = value
