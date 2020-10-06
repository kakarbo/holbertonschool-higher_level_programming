#!/usr/bin/python3
"""Function that creates a class MyList that inherits from list"""


class MyList(list):
    """subclass inheriting from another class or object"""
    def print_sorted(self):
        new_list = sorted(self)
        print(new_list)
