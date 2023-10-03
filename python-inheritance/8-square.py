"""
Represents a square with a given size.

Attributes:
    __size (int): The size of the square (private).
"""
import Rectangle from 7-        
        
class Square(Rectangle):
    """
    Represents a square with a given size.

    Attributes:
        __size (int): The size of the square (private).
    """
    def __init__(self, size):
        """
        Represents a square with a given size.

        Attributes:
            __size (int): The size of the square (private).
        """
        self.__size = super().integer_validator("size", size)
        # super().__init__(size, size)
    def area(self):
        """
        Represents a square with a given size.

        Attributes:
            __size (int): The size of the square (private).
        """
        return self.__size ** 2
        