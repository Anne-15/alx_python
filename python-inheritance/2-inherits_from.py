"""
Represents a function that checks subclass.

"""
def inherits_from(obj, a_class):
    """
    Represents a function that checks subclass.

    """
    obj_class = type(obj)
    return issubclass(obj_class, a_class)