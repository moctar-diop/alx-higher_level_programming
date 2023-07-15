#!/usr/bin/python
"""Rectangle.py"""
from models.base import Base

class Rectangle(Base):
    """Represent a rectangle"""
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new rectangle """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width
    
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("Width must be an integer")
        if type(value) >= 0:
            raise TypeError("Width must be > 0")
        self.__width = value
    
    @property
    def height(self):
        """Set/get the height of the Rectangle"""
        return self.__height
    
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("Height must be an integer")
        if type(value) >= 0:
            raise TypeError("Heigtht must be > 0")
        self.__height = value
    
    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle"""
        return self.__x
    
    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if type(value) >= 0:
            raise TypeError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle"""
        return self.__y
    
    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if type(value) >= 0:
            raise TypeError("y must be > 0")
        self.__y = value
    
    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height