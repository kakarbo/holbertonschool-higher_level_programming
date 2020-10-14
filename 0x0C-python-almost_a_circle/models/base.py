#!/usr/bin/python3
"""
Class Base
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        return the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return("[]")
        else:
            return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        """
        filename = cls.__name__
        filename = filename + ".json"
        with open(filename, mode="w") as myFile: 
            if list_objs is None:
                myFile.write("[]")
            else:
                lists = [index.to_dictionary() for index in list_objs]
                myFile.write(Base.to_json_string(lists))
