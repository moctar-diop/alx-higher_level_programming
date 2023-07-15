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