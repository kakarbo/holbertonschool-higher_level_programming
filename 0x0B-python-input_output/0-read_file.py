#!/usr/bin/python3
"""
function that reads a text file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """
    You must use the with statement
    """
    with open(filename, mode="r", encoding="utf-8") as myFile:
        print(myFile.read())
