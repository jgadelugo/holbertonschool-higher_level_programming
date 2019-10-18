#!/usr/bin/python3
""" class square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class for Square that inherits from rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ initialize """
        super().__init__(size, size, x, y, id)
