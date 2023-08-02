"""
Represents a class of integer validator.

Attributes:
        name (string): The name of the attribute.
        value: to be validated
"""
class BaseGeometry:
    """
    Represents a class

    Attributes:
        name (string): The name of the attribute.
        value: to be validated
    """
    def area(self):
        """
        Represents a function with an exception

        Attributes:
        name (string): The name of the attribute.
        value: to be validated
        """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """
        Represents a function that validates a value

        Attributes:
        name (string): The name of the attribute.
        value: to be validated
        """
        if isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))