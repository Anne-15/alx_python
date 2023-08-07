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

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width
        
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width
        
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
    
    def area(self):
        """
        Represents a function for the area 

        """
        return self.__width * self.__height
    
    def display(self):
        """
        Represents a function that prints the rectangle in #

        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height))
    
    def update(self, *args, **kwargs):
        """
        Represents a function that updates the arguments

        """
        if args and len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

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