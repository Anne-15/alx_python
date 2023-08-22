"""
Import statements
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()

"""
Creating a class
"""

class States(Base):
    """
    Creating table of the class
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = String(128)