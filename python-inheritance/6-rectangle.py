"""
Represents a square with a given size.

Attributes:
    __size (int): The size of the square (private).
"""
class BaseGeometryMeta(type):
    """
    Represents a class
    """
    def __dir__(self):
        """
        Get a list of attributes for this class and exclude
        the __init_superclass

        """
        attributes = super().__dir__()
        new_attributes = [item for item in attributes if item != "__init_subclass__"]
        return new_attributes

class BaseGeometry(metaclass=BaseGeometryMeta):
    """
    Represents a class
    """
    def __dir__(self):
        """
        Get a list of attributes for this class and exclude
        the __init_superclass

        """
        attributes = super().__dir__()
        new_attributes = [item for item in attributes if item != "__init_subclass__"]
        return new_attributes
    
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
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            return value
        
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

        # BaseGeometry.integer_validator("width", width)
        # BaseGeometry.integer_validator("height", height)
