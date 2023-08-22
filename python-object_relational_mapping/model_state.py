from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()
class States(Base):
    """
    Creating a class
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = String(128)