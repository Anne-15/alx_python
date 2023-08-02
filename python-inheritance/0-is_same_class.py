"""
Represents a function that checks subclass.

"""
def is_same_class(obj, a_class):
    """
    Represents a function that checks subclass.

    """
    if issubclass(obj, a_class):
        return True
    else:
        return False