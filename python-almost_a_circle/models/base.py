"""
Represents a base class

"""
class Base:
    """
    Represents a base class

    """
    __nb_object = 0
    def __init__(self, id=None):
        """
        Represents a base class function

        """
        self.id = id
        if id != None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object
