"""
Represents a class.
"""
class BaseGeometry:
    """
    Represents a class
    """
    def area(self):
        """
        Represents a function with an exception
        """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """
        Represents a function that validates a value
        """
        if isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))