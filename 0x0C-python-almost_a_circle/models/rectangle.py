#!/usr/bin/python3
""" Rectangle that inherits Base """
from models.base import Base


class Rectangle(Base):
    """ Rectangle that inherits Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ returns width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """ sets width value """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        returns height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets height value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        returns x value
        """
        return self.x

    @x.setter
    def x(self, value):
        """
        sets x value
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        returns y value
        """
        return self.y

    @y.setter
    def y(self, value):
        """
        sets y value
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        area of a rectangle
        """
        return self.__height * self.__width

    def display(self):
        for v_shift in range(self.__y):
            print()
        for height in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """ string representation of class """
        string = "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(type(self).__name__,
                                                              self.id,self.__x,
                                                              self.__y, self.__width, self.__height)
        return string

    def update(self, *args):
        argCount = len(args)
        if argCount > 0:
            super().__init__(args[0])
        if argCount > 1:
            self.width = args[1]
        if argCount > 2:
            self.height = args[2]
        if argCount > 3:
            self.x = args[3]
        if argCount > 4:
            self.y = args[4]
