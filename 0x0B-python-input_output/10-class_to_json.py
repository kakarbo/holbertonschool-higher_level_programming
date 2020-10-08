#!/usr/bin/python3
"""
function that returns the dictionary description with
simple data structure (list, dictionary, string, integer
and boolean) for JSON serialization of an object:
"""
import json


def class_to_json(obj):
    """
    obj is an instance of a Class
    """
    return(json.dumps(obj, default=lambda o: o.__dict__, sort_keys=True))
