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
        self.size = self.width

    def __str__(self):
        """
        he overloading __str__ method should return
        """
        str1 = "[{}] ({}) ".format(Square.__name__, self.id)
        str2 = "{}/{} - {}".format(self.x, self.y, self.size)
        return(str1 + str2)

    @property
    def size(self):
        """
        the getter
        """
        return(self.width)

    @size.setter
    def size(self, value):
        """
        The setter should assign (in this order) the width
        and the height - with the same value
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        *args is the list of arguments - no-keyworded arguments
        **kwargs can be thought of as a double pointer to a dictionary:
        key/value (keyworded arguments)
        **kwargs must be skipped if *args exists and is not empty
        """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]
        if args is None or len(args) == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        that returns the dictionary representation of a Rectangle:
        """
        dicts = {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "size": self.size}
        return(dicts)
