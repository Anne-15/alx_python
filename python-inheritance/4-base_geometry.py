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

    def __dir__(cls) -> None:
        """
        Get a list of attributes for this class and exclude
        the __init_superclass

        """
        attributes = super().__dir__()
        return [attribute for attribute in attributes if attribute != '__init_superclass']
    
    def area(self):
        """
        Represents a square with a given size.

        Attributes:
            __size (int): The size of the square (private).
        """
        raise Exception("area() is not implemented")