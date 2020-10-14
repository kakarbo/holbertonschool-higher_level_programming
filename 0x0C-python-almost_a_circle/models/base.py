#!/usr/bin/python3
"""
Class Base
"""


class Base:
    """
    Class Base
    """
    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        if len(list_dictionaries) is None:
            return("[]")
        else:
            return(list_dictionaries)
