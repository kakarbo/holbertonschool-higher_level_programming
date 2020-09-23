#!/usr/bin/python3
"""2-square.py
This module makes an empty class Square that defines a square by:
(based on 1-square.py)"""


class Square:
    """an empty class Square that defines a square
    Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0):
    size must be an integer, otherwise raise a TypeError exception
    with the message size must be an integer
    if size is less than 0, raise a ValueError exception eith the
    message size must be >= 0"""
    def __init__(self, size=0):
        """this function instantiates with size private instance attribute"""
        if not isinstance(size, int):
            print("size must be an integer", end="")
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = size
