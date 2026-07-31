#!/usr/bin/python3
"""This module prints text with indentation after specific characters."""


def text_indentation(text):
    """Prints text with two new lines after '.', '?' and ':'"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    previous = ""
    for char in text:
        if char is " " and char is text[0] and previous is "":
            previous = "\n"
            continue
        if char is " " and previous is "\n":
            continue
        if char is "." or char is "?" or char is ":":
            print(char)
            print()
            previous = "\n"
        else:
            print(char, end="")
            previous = char
