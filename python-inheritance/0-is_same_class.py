def is_same_class(obj, a_class):
    if issubclass(obj, a_class):
        return True
    else:
        return False