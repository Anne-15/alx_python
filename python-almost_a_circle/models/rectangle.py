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
            
class Rectangle(Base):
    """
    Represents a class that inherits from base

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Represents a class that inherits from base

        """
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, width):
        self.__width = width
        
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        self.__y = y