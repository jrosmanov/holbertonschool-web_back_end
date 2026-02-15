#!/usr/bin/env python3
"""9-element_length.py"""


def element_length(lst: list) -> list:
    """Returns the length of each element of a list"""
    return [len(i) for i in lst]
