#!/usr/bin/python3
"""
 function that creates an Object from a “JSON file”:
"""
import json


def load_from_json_file(filename):
    """
    You must use the with statement
    ou don’t need to manage exceptions if the JSON string doesn’t
    represent an object.
    """
    with open(filename, mode="r") as myFile:
        return(json.load(myFile))
