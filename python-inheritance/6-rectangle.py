#!/usr/bin/python3

"""
Represents a square with a given size.

Attributes:
    __size (int): The size of the square (private).
"""

"""
Represents a square with a given size.

Attributes:
    __size (int): The size of the square (private).
"""

#BaseGeometry = __import__("sdf")

BaseGeometry =  __import__('5-base_geometry.py').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Represents a square with a given size.

    Attributes:
        __size (int): The size of the square (private).
    """
    def __init__(self, width, height):
        """
        Represents a square with a given size.

        Attributes:
            __size (int): The size of the square (private).
        """
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)
