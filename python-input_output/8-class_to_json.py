#!/usr/bin/python3
"""Module that converts a class instance to a dictionary."""


def class_to_json(obj):
    """Return the dictionary description of an object."""
    return obj.__dict__
