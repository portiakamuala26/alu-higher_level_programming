#!/usr/bin/python3
"""Defines the Rectangle class."""

from models.base import Base


class Rectangle(Base):
    """Represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Gets the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width."""
        self.__width = value

    @property
    def height(self):
        """Gets the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height."""
        self.__height = value

    @property
    def x(self):
        """Gets x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x."""
        self.__x = value

    @property
    def y(self):
        """Gets y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets y."""
        self.__y = value
