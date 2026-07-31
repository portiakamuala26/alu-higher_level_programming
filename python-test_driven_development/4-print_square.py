#!/usr/bin/python3
"""def function to print square"""


def print_square(size):
    """prints square of givensize"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        print("#"*size, end="")
        print()
