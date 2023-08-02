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
            raise TypeError("{} must be an integer".format(self.name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))