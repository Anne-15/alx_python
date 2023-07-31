class Square:
    """
    Represents a square with a given size.

    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def perimeter(self):
        """
        Calculates and returns the perimeter of the square.

        Returns:
            int: The perimeter of the square.
        """
        return 4 * self.__size

    def __str__(self):
        """
        Returns a string representation of the Square object.

        Returns:
            str: A string representation of the Square object.
        """
        return f"Square with size: {self.__size}"