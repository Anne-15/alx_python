"""
Represents an import class

"""
from models.rectangle import Rectangle

"""
Represents a base class

"""
class Square(Rectangle):
    """
    Represents a square class that inherits from rectangle class

    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Represents a function of the square class

        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size))
    
    @property
    def size(self):
        return self.width 
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
        
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.height = value
