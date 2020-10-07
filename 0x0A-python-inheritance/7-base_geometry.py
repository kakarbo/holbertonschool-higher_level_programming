#!/usr/bin/python3
"""class BaseGeometry."""


class BaseGeometry:
    """class BaseGeometry (based on 6-base_geometry.py)."""
    pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method:"""
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
