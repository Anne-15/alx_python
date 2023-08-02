"""
Represents a class.

"""

class BaseGeometry:
    """
    Represents a class
    """
    def __dir__(cls) -> None:
        """
        Get a list of attributes for this class and exclude
        the __init_superclass

        """
        attributes = super().__dir__()
        return [attribute for attribute in attributes if attribute != '__init_superclass']
    pass