#!/usr/bin/python3
def safe_print_integer(value):
    """Print an integer safely."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
