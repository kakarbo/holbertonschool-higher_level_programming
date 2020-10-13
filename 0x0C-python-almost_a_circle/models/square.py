#!/usr/bin/python3
"""
the class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor
        """
        width = size
        height = size
        super().__init__(width, height, x, y, id)
        self.__size = self.width

    def __str__(self):
        """
        he overloading __str__ method should return
        """
        str1 = "[{}] ({}) ".format(Square.__name__, self.id)
        str2 = "{}/{} - {}".format(self.x, self.y, self.__size)
        return(str1 + str2)

    @property
    def size(self):
        """
        the getter
        """
        return(self.__size)

    @size.setter
    def size(self, value):
        """
        The setter should assign (in this order) the width
        and the height - with the same value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__size = value
