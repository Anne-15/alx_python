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