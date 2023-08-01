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
        self.__size = size
        if type(size) != int:
            print("Size must be an integer")
        elif size < 0:
            print("Size must be >=0")