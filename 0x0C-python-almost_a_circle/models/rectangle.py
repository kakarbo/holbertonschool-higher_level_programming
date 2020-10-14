#!/usr/bin/python3
"""
Class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle that inherits from Base:
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        the class Rectangle that inherits from Base:
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        the class Rectangle by adding validation of
        all setter methods and instantiation (id excluded):
        """
        return(self.__width)

    @width.setter
    def width(self, value):
        """
        the class Rectangle by adding validation of
        all setter methods and instantiation (id excluded):
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        the class Rectangle by adding validation of
        all setter methods and instantiation (id excluded):
        """
        return(self.__height)

    @height.setter
    def height(self, value):
        """
        the class Rectangle by adding validation of
        all setter methods and instantiation (id excluded):
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        the class Rectangle by adding validation of
        all setter methods and instantiation (id excluded):
        """
        return(self.__x)

    @x.setter
    def x(self, value):
        """
        the class Rectangle by adding validation of
        all setter methods and instantiation (id excluded):
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        the class Rectangle by adding validation of
        all setter methods and instantiation (id excluded):
        """
        return(self.__y)

    @y.setter
    def y(self, value):
        """
        the class Rectangle by adding validation of
        all setter methods and instantiation (id excluded):
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        the class Rectangle by adding the public method def
        area(self): that returns the area value of the
        Rectangle instance.
        """
        return(self.__width * self.__height)

    def display(self):
        """
        class Rectangle by adding the public method def
        display(self): that prints in stdout the Rectangle
        instance with the character
        # - you don’t need to handle x and y here.
        """
        str1 = "".join(" " * self.__x)
        str2 = "".join("#" * self.__width)
        for index in range(self.__y):
            print()
        for index in range(self.__height):
            print(str1 + str2)

    def __str__(self):
        """
        the class Rectangle by overriding
        the __str__ method so that it returns
        """
        str1 = "[{}] ({}) ".format(Rectangle.__name__, self.id)
        str2 = "{}/{} - ".format(self.__x, self.__y)
        return(str1 + str2 + "{}/{}".format(self.__width, self.__height))

    def update(self, *args, **kwargs):
        """
        the class Rectangle by improving the public
        method def display(self):
        """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.__width = args[1]
        if len(args) > 2:
            self.__height = args[2]
        if len(args) > 3:
            self.__x = args[3]
        if len(args) > 4:
            self.__y = args[4]
        if args is None or len(args) == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """
        that returns the dictionary representation of a Rectangle:
        """
        dicts = {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "width": self.width,
            "height": self.height}
        return(dicts)
