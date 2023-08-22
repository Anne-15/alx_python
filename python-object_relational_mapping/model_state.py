#!/usr/bin/python3
"""
Module containing the State class definition and Base instance
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class State(Base):
    """
    Represents a State class that inherits from Base
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://username:password@localhost:3306/dbname")
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
