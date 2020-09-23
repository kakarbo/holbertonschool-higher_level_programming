#!/usr/bin/python3
"""6-square.py
This module makes an empty class Square that defines a square by:
(based on 5-square.py)"""


class Square:
    """class Square that defines a square by:
    (based on 5-square.py)
    Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError
exception with the message size must be an integer
if size is less than 0, raise a ValueError exception
with the message size must be >= 0"""
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            print("size must be an integer")
            raise TypeError
        elif size < 0:
            print("size must be >= 0")
            raise ValueError
        else:
            self.__size = size
            self.__position = position

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
            raise TypeError
        elif value < 0:
            print("size must be >= 0")
            raise ValueError
        else:
            self.__size = value

    @property
    def position(self):
        return(self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value, int):
            print("position must be a tuple of 2 positive integers")
            raise TypeError
        elif value < 0:
            print("size must be >= 0")
            raise ValueError
        else:
            self.__position = value

    def area(self):
        return(self.__size ** 2)

    def my_print(self):
        import sys
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                print()
            for i in range(self.__size):
                if self.__position[0] != 0:
                    for a in range(self.__position[0]):
                        print(" ", file=sys.stdout, end="")
                for x in range(self.__size):
                    print("#", file=sys.stdout, end="")
                print()
