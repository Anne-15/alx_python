"""
Represents the use of sqlalchemy orm.

"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()

"""
Represents a square with a given size.

Attributes:
    __size (int): The size of the square (private).
"""
class States(Base):
    """
    Represents a square with a given size.

    Attributes:
        __size (int): The size of the square (private).
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = String(128)