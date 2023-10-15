"""
Represents a function that checks subclass.

"""


def inherits_from(obj, a_class):
    """
    Represents a function that checks subclass.

    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
