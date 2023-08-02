"""
Represents a function that checks subclass.

"""

def inherits_from(obj, a_class):

    """
    Represents a function that checks subclass.

    """

    if issubclass(obj, a_class):
        return True
    else:
        return False