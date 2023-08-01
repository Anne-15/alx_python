"""
Represents a square with a given size.

Attributes:
    __size (int): The size of the square (private).
"""
class Square:
    """
    Represents a square with a given size.

    Attributes:
        __size (int): The size of the square (private).
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        return self.__size ** 2
    def size(self):
        return self.__size
    def size(self, size):
        self.__size = size