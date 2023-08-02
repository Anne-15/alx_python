"""
Represents a square with a given size.

Attributes:
    __size (int): The size of the square (private).
"""
class BaseGeometry:
    """
    Represents a square with a given size.

    Attributes:
        __size (int): The size of the square (private).
    """
    def area(self):
        """
        Represents a square with a given size.

        Attributes:
            __size (int): The size of the square (private).
        """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """
        Represents a square with a given size.

        Attributes:
            __size (int): The size of the square (private).
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        
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
        self.__width = width
        self.__height = height

        BaseGeometry.integer_validator(self, width, value=0)
        BaseGeometry.integer_validator(self, height, value=0)
