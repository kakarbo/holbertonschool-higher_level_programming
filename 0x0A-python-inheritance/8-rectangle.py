#!/usr/bin/python3
"""class BaseGeometry."""


class BaseGeometry:
    """class BaseGeometry (based on 7-base_geometry.py)."""
    def area(self):
        """Public instance method:"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method:"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        self.__height = height
        self.__width = height
        try:
            integer_validator(width, height)
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))
